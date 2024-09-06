```python
def is_prime(n):
    """
    Check if a number is prime.
    >>> returns True if the thought by that n is a prime number, and False otherwise.
    """
    function implements an primality test using the Sieve of Eratosthenes algorithm.
    """
    `A if n < 2 or n > 2 ** 3`:**
        return False
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
```