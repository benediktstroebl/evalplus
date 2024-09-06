def is_prime(n):
    """ Checks if a number is prime """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def hex_key(num):
    """Counts the number of hexadecimal digits that are primes"""
    hex_digits = '0123456789ABCDEF'
    count = 0
    for digit in num:
        if hex_digits.index(digit) < 16:
            if is_prime(int(digit)):
                count += 1
    return count