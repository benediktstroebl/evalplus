def is_prime(num):
    """
    Checks if a number is a prime number
    """
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True
def hex_key(num):
    """
    Counts the number of hexadecimal digits that are primes
    """
    prime_digits = 0
    num = str(num)
    for digit in num:
        if digit in '2 3 5 7 B D':
            prime_digits += 1
        elif is_prime(int(digit)):
            prime_digits += 1
    return prime_digits