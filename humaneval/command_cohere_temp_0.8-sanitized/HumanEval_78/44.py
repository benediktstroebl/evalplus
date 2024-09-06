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
    digits = ['0','1','2','3','4','5','6','7','8','9', 'A', 'B', 'C', 'D', 'E', 'F']
    digits = [int(d) for d in digits]
    if isinstance(num, str) and num:
        for digit in num:
            if digits.index(digit) >= 0:
                if is_prime(digits[digits.index(digit)]):
                    count += 1
    return count