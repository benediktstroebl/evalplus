```python
import math

def is_prime(n):
    """Check if a number is a prime."""
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def hex_key(num):
    """Count the number of hexadecimal digits that are primes."""
    # Convert hexadecimal string to integer to simplify computations
    num = int(num, 16)
    count = 0
    for digit in str(num):
        if digit in '2 3 5 7 B D':  # Corrected comparison with decimal values
            count += is_prime(int(digit))
    return count
```

The `is_prime` function is used to determine if a given number is prime. This function checks if the number is less than or equal to 1, as prime numbers always exceed 1; it then iterates from 2 up to the square root of the number and checks if the number is divisible by any of these integers. If the number is not divisible by any of them, the function returns `True`, indicating that the number is prime. 

The `hex_key` function takes a hexadecimal number as input and counts the number of hexadecimal digits that are primes. It does this by first converting the hexadecimal string to an integer and then iterating through each digit in the decimal representation of the number. It includes 'B' and 'D' in the comparison, converted to their decimal values. For each digit that is one of the prime hexadecimal digits ('2', '3', '5', '7', 'B', or 'D'), it checks if the digit is prime using the `is_prime` function and increments the count if it is. Finally, the function returns the total count of prime hexadecimal digits. 

This solution assumes that the input is always correct, and the prime digits A, B, C, D, E, F are always uppercase.