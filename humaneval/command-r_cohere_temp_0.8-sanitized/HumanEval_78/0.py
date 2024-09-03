def hex_key(hex_str):
    """Count prime hexadecimal digits in hex_str."""
    primes = 0
    for digit in hex_str:
        if digit in '2357BD':
            primes += 1
    return primes