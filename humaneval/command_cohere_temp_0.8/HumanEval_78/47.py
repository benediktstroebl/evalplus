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
    digits = "0123456789ABCDEF"
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

The approach used by the `hex_key` function is as follows:
1. We first convert all uppercase hexadecimal digits to their corresponding decimal values, using the `find` method for uppercase digits and converting the lowercase digits directly.
2. We then use the internal `is_prime` function to check if the decimal value of each digit is prime.
3. Finally, we tally the count of all prime digits.

Here is how the script performs on a few test cases:
```python
print(hex_key("AB"))  # Output: 1
print(hex_key("1077E"))  # Output: 2
print(hex_key("ABED1A33"))  # Output: 4
print(hex_key("123456789ABCDEF0"))  # Output: 6
print(hex_key("2020"))  # Output: 2
```

This script should correctly determine the count of prime hexadecimal digits in the given input string.