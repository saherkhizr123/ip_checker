
```python
import ipaddress


def check_ip(ip_address):
    try:
        ip = ipaddress.ip_address(ip_address)

        print("\nIP Address:", ip)
        print("Version: IPv" + str(ip.version))

        if ip.is_private:
            print("Type: Private")
            print("Used mainly inside local networks.")
        else:
            print("Type: Public")
            print("Can be used on the public internet.")

    except ValueError:
        print("\nInvalid IP address.")
        print("Please enter a valid IPv4 or IPv6 address.")


print("=" * 35)
print("       IP Address Checker")
print("=" * 35)

user_input = input("Enter an IP address: ").strip()

check_ip(user_input)
```
