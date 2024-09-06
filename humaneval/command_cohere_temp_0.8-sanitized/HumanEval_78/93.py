import math
def is_prime(n):
    """
    Checks if a number is prime
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def hex_key(num):
    """
    Counts the number of hexadecimal digits that are primes
    """
    # your code here
    digit_primes = 0
    num = str(num)
    # Assuming input is always correct or empty string
    # removing non-hexadecimal digits and converting to uppercase
    num = ''.join(c for c in num if c in '0123456789ABCDEF')
    num = num.upper()
    for digit in num:
        if is_prime(int(digit)):
            digit_primes += 1
    return digit_primes