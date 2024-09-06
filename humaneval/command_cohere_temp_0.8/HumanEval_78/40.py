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
    hex_digits = "0123456789ABCDEF"
    count = 0
    for digit in num:
        if digit in hex_digits and is_prime(int(digit)):
            count += 1
    return count
```

The provided Python script defines a function `hex_key` that solves the problem statement. It iterates through each digit in the input hexadecimal number and checks if each digit is a prime number. The function returns the count of prime digits in the input hexadecimal number.

Also, the script includes a separate function `is_prime` for primality testing, which is used by `hex_key` to determine if a digit is prime or not. The `is_prime` function iterates through the numbers from 2 to the square root of the number and checks for divisibility. If the number is divisible by any integer within this range, it is not a prime; otherwise, it is a prime number.