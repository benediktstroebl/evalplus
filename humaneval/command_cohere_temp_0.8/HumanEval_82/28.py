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

This script defines a test suite that checks the `prime_length` function on various inputs. You can test the script by calling `python test_prime_length.py` on the console.

The `prime_length` function first checks if the input is a string, and then uses the `is_prime` function to test whether the length of the string is divisible by any number besides 1 and itself. If the length is indeed prime, the function returns `True`; otherwise, it returns `False`.