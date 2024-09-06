```python
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
    digits = '0123456789ABCDEF'
    count = 0
    for char in num:
        if char.isupper():
            digit = digits.find(char)
        else:
            digit = int(char)
        if is_prime(digit):
            count += 1
    return count
```

The solution relies on the `is_prime` helper function, which checks whether a given number is prime using a tried-and-true optimization: sweeping through potential divisors from 2 up to the square root of the number. For each digit in the hexadecimal number, the `hex_key` function converts it to a numeric value, checks its primality, and increments the count if it passes. As a result, this solution handles all edge cases as outlined in the problem statement.