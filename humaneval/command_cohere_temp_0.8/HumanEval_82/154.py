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

This script defines a function `is_prime(x)` that checks whether a given number `x` is prime. It employs a optimized strategy by checking only the divisibility of `x` by integers from 2 to the square root of `x`. 

The second function, `prime_length(string)`, first validates that the input is a string and then uses `is_prime()` to determine whether the length of the string is prime. This aligns with the `prime_length()` function's purpose of returning `True` if the string length is prime and `False` otherwise. 

Both functions are standalone, and the `prime_length()` function can be used directly to test for string lengths being prime. 

This solution has a time complexity of O(sqrt(n)) for the `is_prime()` function, due to its optimized checking mechanism that cuts off the checking at the square root of the number. 

The total time complexity of the full `prime_length()` function is O(sqrt(n)) as it only calls `is_prime()` once.