def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def hex_key(num):
    """Count the number of hexadecimal digits that are primes."""
    digit_primes = 0
    for char in num:
        if char.isupper():
            digit = int(char)
            if is_prime(digit):
                digit_primes += 1
    return digit_primes