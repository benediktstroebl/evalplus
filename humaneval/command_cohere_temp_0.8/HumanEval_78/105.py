```python
import math

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def hex_key(num):
    """Count the number of hexadecimal digits that are primes."""
    hex_digits = '0123456789ABCDEF'
    count = 0
    for digit in num:
        if digit in hex_digits and is_prime(int(digit)):
            count += 1
    return count
```

The provided Python script defines a function `hex_key` that solves the problem statement. It accepts a hexadecimal number as input and calculates the number of hexadecimal digits that are prime numbers.

The script also incorporates a helper function, `is_prime`, which checks whether a given number is a prime. This function is used to determine the primality of each digit in the hexadecimal number.

Furthermore, the script includes a list comprehension that iterates through each digit in the hexadecimal number and evaluates whether it is a prime number. If the digit is prime, it increments the count variable. Finally, the function returns the total count of prime hexadecimal digits.