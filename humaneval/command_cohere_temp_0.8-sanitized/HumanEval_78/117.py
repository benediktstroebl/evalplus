import math
def is_prime(n):
    """Check is n is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def hex_key(num):
    """Count the number of hexadecimal digits that are primes."""
    # your code here
    count = 0
    digits = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
        '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13,
        'E': 14, 'F': 15
    }
    if num == "":
        return 0
    for digit in num:
        if digits[digit] in range(2, 17):
            count += digits[digit] == math.floor(math.sqrt(digits[digit])) and is_prime(digits[digit])
    return count