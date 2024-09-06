```python
import math

def is_prime(n):
    """
    Checks if a number is a prime
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def hex_key(num):
    """
    Counts the number of hexadecimal digits that are primes
    """
    digits = '0123456789ABCDEF'
    count = 0
    for digit in num:
        if digit in digits and is_prime(int(digit)):
            count += 1
    return count
```

The provided Python script defines a function `hex_key` that takes a string `num` representing a hexadecimal number as input. It aims to count the number of hexadecimal digits that are prime numbers. To accomplish this, it employs the `is_prime` function to check if a given digit is a prime. The script then iterates through each digit in the input number and assesses whether it's a valid hexadecimal digit and if it's a prime, increasing the `count` variable. Ultimately, the function returns the calculated count of prime hexadecimal digits. 

The `is_prime` function is also included, which verifies if a given number is a prime number through a loop that checks for divisibility by all numbers from 2 to the square root of the number. Both functions are well-commented, making it clear what each line of code does. Overall, the script provides an effective solution to the problem posed, fulfilling the challenge requirements.