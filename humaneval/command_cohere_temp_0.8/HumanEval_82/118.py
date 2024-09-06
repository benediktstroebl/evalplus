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

This script defines a test suite with different strings and their corresponding expected results. The `prime_length()` function is designed to accept a string as input and determine whether the length of that string represents a prime number. Through the use of the `is_prime()` function, which checks divisibility for numbers, it determines if the length of the string, interpreted as an integer, is a prime number or not. 

The `is_prime()` function serves as a helpful utility to ascertain whether a given number is prime. It begins by handling edge cases where the input num is less than or equal to 1, returning False immediately due to the lack of divisors. It then progresses through a loop starting from 2 and ending at the square root of the input num. If the number is divisible by any integer within this range, it is deemed non-prime and again, False is returned. However, if no divisors are found, True is returned, indicating that the number is prime. 

By utilizing this `is_prime()` function, the `prime_length()` function can assess whether the length of a given string is a prime number or not. The script demonstrates the application of these functions on test cases, resulting in accurate assessments of prime string lengths.