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

The solution algorithm is the following:
1. Firstly, the function `is_prime(n)` checks whether a given number `n` is a prime number or not. If the number is less than 2 or has a divisor within the range from 2 to its square root, then it is not prime; otherwise, it is prime. 
2. Secondly, for each character of the input string `num` the function `hex_key()` does the following:
    - If the character is uppercase, it indexes the `digits` string to get its decimal equivalent. 
    - If the character is lowercase, it takes it as an integer. 

Finally, the function counts the digits that pass the `is_prime()` function test and returns the total count. 

Note that the `digits` string contains all hexadecimal digits.