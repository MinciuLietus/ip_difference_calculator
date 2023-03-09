# Installation
Before installing the program, please ensure that you have Python 3 installed on your machine. You can download Python 3 from the official website: https://www.python.org/downloads/.

Once you have Python 3 installed, you can either clone the repository or download the code in ZIP file format.

# Usage
To run the program, execute the following command in the command-line interface (CLI):
```
python compare_ips.py first_ip second_ip [--ipv4] [--ipv6]
```

You can compare IPV4 addresses or IPV6 addresses by passing the --ipv4 or --ipv6 arguments. Here's an example:

For IPV4
```
python compare_ips.py 10.0.0.0 10.0.0.50 --ipv4
```

Output:
```
"10.0.0.0" "10.0.0.50" => 50
```

For IPV6
```
python compare_ips.py 2001:0db8:0000:0000:0000:8a2e:0370:7334 2001:0db8:0000:0000:0000:8a2e:0370:7555 --ipv6
```

Output:
```
"2001:0db8:0000:0000:0000:8a2e:0370:7334" "2001:0db8:0000:0000:0000:8a2e:0370:7555" => 545
```
