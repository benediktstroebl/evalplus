```python
import math

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def hex_key(num):
    """Count the number of hexadecimal digits that are primes."""
    # Convert hex string to decimal numbers
    num = int(num, 16)
    digits = []
    while num > 0:
        digit = num % 16
        digits.append(digit)
        num = num // 16
    # Count primes among the digits
    count = sum(1 for digit in digits if is_prime(digit))
    return count
```

The code first converts the hexadecimal string to decimal numbers and retrieves each digit. Then, it uses a `generator expression` in the sum function to iterate through the digits and check if they are prime – this technique is used to enhance code readability and conciseness. The `is_prime` function is introduced to check whether a given number is prime or not.

The code is concise, and it correctly determines the number of prime hexadecimal digits in the given hexadecimal number.