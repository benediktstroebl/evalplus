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

This Python script defines a function `prime_length` that takes a string as an input and returns a boolean value (`True` or `False`) depending on whether the length of the string is a prime number or not. This function is tested on various strings and is designed to work correctly on all of them.