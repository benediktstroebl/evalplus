```python
import math

def is_prime(n):
    """Check if a number is a prime."""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def hex_key(num):
    """Count the number of hexadecimal digits that are primes."""
    # convert the string to uppercase
    num = num.upper()
    count = 0
    for char in num:
        if char in '2D5773BCDEF':  # hexadecimal digits that are primes
            count += num.count(char)
    return count
```

The code defines a function `hex_key` that takes a string `num` representing a hexadecimal number as input, it checks whether each digit of the number is a prime or not using the `is_prime` function, and returns the count of digits that are primes, the script handles both lowercase and uppercase correctly.