def is_prime(num):
    """
    Checks if a number is a prime
    """
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def hex_key(num):
    """
    Counts the number of hexadecimal digits that are primes
    """
    prime_count = 0
    for digit in num:
        if digit.isdigit():
            digit = int(digit)
        if is_prime(digit):
            prime_count += 1
    return prime_count