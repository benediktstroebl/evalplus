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
    hex_digits = '0123456789ABCDEF'
    count = 0
    for char in num:
        if char.isupper():
            digit = hex_digits.find(char)
        else:
            digit = int(char)
        if is_prime(digit):
            count += 1
    return count
```

The provided Python script defines a function `hex_key` that solves the problem statement. It takes a hexadecimal number as input and counts the number of hexadecimal digits that are primes. 

The script also includes a helper function, `is_prime`, which checks whether a given number is a prime. It iterates through the numbers from 2 to the square root of the input number and checks for divisibility. If the number is divisible by any integer within this range, it returns `False`. If not, it confirms the number as prime and returns `True`. 

The `hex_key` function processes each character of the input number. It identifies uppercase letters and converts them to their corresponding decimal values using the `find` method. For non-uppercase digits, it assumes they are already in decimal form. 

The function then calls the `is_prime` helper function to check if each digit is a prime. If so, it increments the count, and finally, it returns the total count of prime hexadecimal digits. 

Note that this code assumes the input is always correct, as mentioned in the original problem statement. It means that all mentioned assumptions and scenarios will behave as expected. Also, this version has an insignificant computational cost for the prime checking function for typical inputs because the largest possible hex digit is 127, and the square root of 127 is 127.1 with an integer result. So, the loop will never iterate beyond 127.