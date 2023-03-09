import sys

ONE_SET_BIT_SIZE = 16
ALLOWED_VERSIONS = {"ipv4": "ipv4", "ipv6": "ipv6"}

IPV6_CHARACTER_MAP = {
    "A": 10,
    "B": 11,
    "C": 12,
    "D": 13,
    "E": 14,
    "F": 15,
}


def main(first_ip, second_ip, ip_ver):
    function_map = {"ipv4": calculate_ipv4, "ipv6": calculate_ipv6}

    result = 0
    function = function_map.get(ip_ver)

    if function:
        result = function(first_ip, second_ip)

    if result < 0:
        print("Last IP address must be greater than the first one.")
        sys.exit(0)

    return f'"{first_ip}" "{second_ip}" => {result if result else ""}'


def calculate_ipv4(first_ip, second_ip):
    first_ips = [int(val) for val in first_ip.split(".")]
    second_ips = [int(val) for val in second_ip.split(".")]

    first_ip_decimal = ipv4_address_to_decimal(*first_ips)
    second_ip_decimal = ipv4_address_to_decimal(*second_ips)

    return second_ip_decimal - first_ip_decimal


def calculate_ipv6(first_ip, second_ip):
    first_ips = [val for val in first_ip.split(":")]
    second_ips = [val for val in second_ip.split(":")]

    first_ip_decimal = ipv6_address_to_decimal(*first_ips)
    second_ip_decimal = ipv6_address_to_decimal(*second_ips)

    return second_ip_decimal - first_ip_decimal


def ipv4_address_to_decimal(*args):
    result = 0
    ipv4_bit_size = 256
    starting_point = len(args)

    for h in args:
        starting_point = starting_point - 1
        result += h * ipv4_bit_size**starting_point

    return result


def ipv6_address_to_decimal(*args):
    result = 0
    decimal_representation = tuple(
        convert_ipv6_set_chars(hexadecimal) for hexadecimal in args
    )
    starting_point = len(decimal_representation) * ONE_SET_BIT_SIZE

    for h in decimal_representation:
        starting_point = starting_point - ONE_SET_BIT_SIZE
        result += (2**starting_point) * h

    return result


# Function that converts a set of hexadecimal characters to decimal
def convert_ipv6_set_chars(hexadecimal):
    result = 0
    hexadecimals = []

    for char in hexadecimal:
        if (key := char.upper()) in IPV6_CHARACTER_MAP.keys():
            char = IPV6_CHARACTER_MAP[key]
        hexadecimals.append(int(char))

    tup = tuple(hexadecimals)
    starting_point = len(tup)

    for h in tup:
        starting_point = starting_point - 1
        result += ONE_SET_BIT_SIZE**starting_point * h

    return result


if __name__ == "__main__":
    wrong_arg_msg = "Usage: compare_ips.py first_ip second_ip [--ipv4] [--ipv6]"
    try:
        first_ip_arg, second_ip_arg, version_key = sys.argv[1], sys.argv[2], sys.argv[3]
    except Exception:
        print("Unexpected arguments. Try again.\n", wrong_arg_msg)
        sys.exit(0)

    ip_version = ALLOWED_VERSIONS.get(version_key.strip("--").lower())

    if not ip_version:
        print("Selected version is not compatible.")
        sys.exit(0)

    ips = first_ip_arg, second_ip_arg

    try:
        final_result = main(*ips, ip_version)
    except ValueError:
        print(f"The {ip_version.upper()} address format is invalid.")
        sys.exit(0)

    print(final_result)
