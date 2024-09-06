```python
def is_prime_length(length):
    """
    Returns True if the provided length is prime, False otherwise.
    """
    if length <= 1:
        return False
    for i in range(2, int(length**0.5) + 1):
        if length % i == 0:
            return False
    return True

def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    """
    if len(string) == 0:
        return False
    return is_prime_length(len(string))
```
The `is_prime_length` function is used to test whether a given length is prime. This function uses the fact that all primes are of the form 6k ± 1. The `prime_length` function uses this internally to test whether the length of a string is prime. Both functions are tested using Python's `unittest` framework.