def is_prime(n):
    """Checks if a number is a prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def hex_key(num):
    """Count the number of hexadecimal digits that are primes."""
    # your code here
    digit = '0123456789ABCDEF'
    count = 0
    for char in num:
        if char.isupper():
            digit = 'ABCDEF'
        else:
            digit = '0123456789'
        if digit[int(char)] in '23579BDEF':
            continue
        if is_prime(int(char)):
            count += 1
    return count