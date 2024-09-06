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

This script defines a function `is_prime(x)` that checks whether a given number `x` is prime. It employs a simple optimization by checking only up to the square root of `x`, rather than checking all numbers up to `x`. For any non-prime number `x`, there always exists at least one integer `y` such that `y * y` equals `x` or `x - 1`. 

The `prime_length(string)` function first validates that the input is a string and then uses the `is_prime()` function to check whether the length of the string is a prime number. The function returns `True` if the string length is prime and `False` otherwise. This approach eliminates the need to implement separate functions to handle various edge cases. 

You can test this function against the examples in the prompt statement by calling `prime_length()` with different strings.