Here is a Python script with a self-contained function that solves the problem and passes the tests:
```python
def is_prime(n):
    """
    Checks if a number is prime.
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def hex_key(num):
    """
    Counts the number of hexadecimal digits that are primes.
    """
    hex_digits = "0123456789ABCDEF"
    count = 0
    for digit in num:
        if hex_digits.index(digit) in [2, 3, 5, 7, 11, 13]:
            count += 1
    return count
```

This script includes a function `hex_key` that solves the problem as described in the prompt. It also includes a helper function `is_prime` that checks whether a given number is prime or not. 

You can test this script by providing different hexadecimal numbers as input to see how many hexadecimal digits that are primes it counts for each number.