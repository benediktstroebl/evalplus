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
    # Convert hex string to decimal numbers
    num = int(num, 16)
    digits = []
    while num > 0:
        digits.append(num % 16)
        num //= 16
    # Filter out non-prime digits and count
    count = sum(1 for digit in digits if is_prime(digit))
    return count
```
The `is_prime` function is used to determine if a number is prime. This function uses a basic optimization of excluding the possibility of a number being divisible by any integer less than or equal to its square root. The `hex_key` function converts the hexadecimal string to decimal integers, and then loops through each digit, converting it to an integer and checking if it's prime. The function then gives back the count of prime digits.

This solution assumes that the input is always correct or an empty string, and that symbols A, B, C, D, E, F are always uppercase.

The provided examples in the problem statement result in the following outputs:
- `num = "AB"` : 1
- `num = "1077E"` : 2
- `num = "ABED1A33"` : 4
- `num = "123456789ABCDEF0"` : 6
- `num = "2020"` : 2