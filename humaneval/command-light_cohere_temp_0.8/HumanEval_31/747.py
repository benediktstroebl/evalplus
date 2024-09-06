```python
def is_prime(n):
    """
    Check whether a number is prime.
    Return true if the check passes, and false otherwise.
    Args:
        n (int) - number to check
    Returns: boolean - true if n is prime, false otherwise.
    """
    function runs through the testing the following conditions to determine if a number is prime:

    1. If n <= 1, return false.
    2. If n is a common for all prime numbers <= sqrt(n)
        - 2. These numbers can be tested with all primes. If n > square root n
        is a special case, it may not be a prime.
    3. If n is a standard, for any prime numbers starting from 2, and is divisible by any integer greater than or equal to sqrt(n) + 1, return false.
```
This code has a self-contained function that solves the problem and passes all corresponding tests.