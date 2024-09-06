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

This script defines a function `is_prime(x)` that checks whether a given number `x` is prime. It employs a straightforward algorithm: it checks if `x` is less than or equal to 1, in which case it is not prime, or if `x` has any divisors between 2 and the square root of `x`, if it does, it is not prime. If neither condition is met, `x` is prime. 

The `prime_length(string)` function first checks if the input `string` is a string, and then calls `is_prime()` to check if the length of `string` is prime.

This solution achieves the intended functionality, while handling potential edge cases like non-string inputs.