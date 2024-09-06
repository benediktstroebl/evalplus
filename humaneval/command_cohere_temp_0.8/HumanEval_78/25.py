```python
import math

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def hex_key(num):
    """Count the number of hexadecimal digits that are primes."""
    # Convert hex strings to decimal numbers
    decimal = {char: int(char, 16) for char in num}
    total = 0
    for digit in decimal.values():
        if is_prime(digit):
            total += 1
    return total
```

The approach is to:
1. Convert the hexadecimal number to decimal numbers and store them in a dictionary where the keys are the hexadecimal digits and the values are the corresponding decimal numbers.
2. Use the existing `is_prime` function to check if each decimal number is prime.
3. Count the digits that are prime and return the total.

The `is_prime` function checks if a given number is prime by iterating from 2 up to the square root of the number. If the number is divisible by any integer within this range it is not a prime, otherwise, it is a prime number.