import ipaddress

def check_ip_type():
    print("=" * 35)
    print("   IP Address Type Checker")
    print("=" * 35)
    
    # Take input from the user
    user_input = input("Enter an IP address to check: ").strip()
    
    try:
        # The ip_address function validates and creates an IP object
        ip = ipaddress.ip_address(user_input)
        
        # Check if the IP is private or public
        if ip.is_private:
            print(f"\nResult: {ip} is a PRIVATE IP address.")
            print("💡 Private IPs are used inside local networks (like your home Wi-Fi).")
        else:
            print(f"\nResult: {ip} is a PUBLIC IP address.")
            print("🌐 Public IPs are used to identify devices across the global internet.")
            
    except ValueError:
        # This catches typos or invalid IP formats (e.g., 999.999.999.999 or "hello")
        print("\n❌ Error: Invalid IP address format. Please try again.")
    
    print("=" * 35)

if __name__ == "__main__":
    check_ip_type()
