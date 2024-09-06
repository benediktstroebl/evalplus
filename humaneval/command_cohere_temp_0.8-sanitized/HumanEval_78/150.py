import math
def is_prime(n):
    """Check if a number is a prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def hex_key(num):
    """Count the number of hexadecimal digits that are primes."""
    # convert the string to uppercase
    num = num.upper()
    count = 0
    for digit in num:
        if digit in '2 3 5 7 B D': 
            continue
        # Check if the digit is a decimal, and if so convert it to an integer
        # and check if it is a prime.
        if digit in '8 9 A B C D E F':
            digit = int(digit)
        if is_prime(digit):
            count += 1
    return count