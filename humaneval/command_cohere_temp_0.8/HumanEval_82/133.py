```python
def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    """
    if not isinstance(string, str):
        return False
    return is_prime(len(string))
```

This Python code defines a function `is_prime(num)` that checks whether a given number is prime or not. It handles edge cases where `num` is less than or equal to 1, and then iterates from 2 to the square root of the number, checking for divisibility. If no divisors are found, the function returns `True`, indicating that the number is prime. The second function, `prime_length(string)`, first verifies that the input is a string and then uses `is_prime()` to determine if the length of the string is a prime number, returning a boolean value accordingly. 

This solution passes the provided tests.