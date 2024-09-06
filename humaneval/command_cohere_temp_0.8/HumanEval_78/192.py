```python
import math

def is_prime(n):
    """Check is n is prime."""
    if n <= 1:
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
        if digit in hex_digits and is_prime(int(digit, 16)):
            count += 1
    return count
```

The provided Python script defines a function `hex_key` that solves the problem statement. It takes a hexadecimal number as input and counts the number of hexadecimal digits that are prime numbers.

The `is_prime` function is introduced to check whether a given number is prime or not. It iterates through the numbers from 2 to the square root of the input number and checks for divisibility. If the number is divisible by any integer within this range, it is not prime; otherwise, it is considered prime.

The `hex_key` function initializes a count variable to zero and iterates through each digit of the input hexadecimal number. For each digit, it checks if it's a valid hexadecimal digit and if it's prime. If so, it increments the count. Finally, it returns the total count of prime hexadecimal digits.

The script assumes that the input is always correct or empty, and all symbols are in uppercase. The given examples in the problem statement are correctly solved by the script, and the output matches the expected result for each case.

This code has no dependencies other than the Python standard library, making it self-contained and easy to use in any Python environment.  It should help solve the problem statement correctly.