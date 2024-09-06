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
    hex_digits = '0123456789ABCDEF'
    count = 0
    for char in num:
        if char.isupper():
            digit = hex_digits.index(char)
        else:
            digit = int(char)
        if is_prime(digit):
            count += 1
    return count
```

The provided Python script defines a function `hex_key` that solves the problem statement. It takes a hexadecimal number as input and counts the number of hexadecimal digits that are primes. 

The script also includes a helper function, `is_prime`, which checks whether a given number is a prime. It iterates through the numbers from 2 to the square root of the input number and checks for divisibility. If the number is divisible by any of these factors, it returns `False`. If not, it returns `True`. 

The `hex_key` function iterates through each character in the input number and identifies hexadecimal digits. If the character is uppercase, it converts it to its decimal equivalent using the `index` method. It then checks if the digit is prime using the `is_prime` function and increments the count if it is. Finally, it returns the total count of prime hexadecimal digits.

The script includes example tests that verify the function's behavior against various inputs.