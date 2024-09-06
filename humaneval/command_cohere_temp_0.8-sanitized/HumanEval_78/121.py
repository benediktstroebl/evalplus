def is_prime(n):
    """
    Checks if a number is prime.
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def hex_key(num):
    """
    Counts the number of hexadecimal digits that are primes.
    """
    digit_primes = 0
    for char in num:
        if char.isupper():
            digit = ord(char) - ord('A') + 10
            if is_prime(digit):
                digit_primes += 1
    return digit_primes