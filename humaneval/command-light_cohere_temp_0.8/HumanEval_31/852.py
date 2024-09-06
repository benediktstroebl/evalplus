```python
def is_prime(n):
    """
    Check if a number is prime.
    >>> returns True if n is prime, False otherwise.
    >>> is_prime(6)  # Test for 6
    False
    >>> is_prime(7)  # Test for prime 7
    True
    >>> is_prime(10)  # Test for non-prime 10
    False
    >>> is_prime(1344)  # Test for a large number
    True
    >>> is_prime(2)  # Test for even number
    False
    >>> is_prime(1)  # Test for smallest prime
    True
    """
    # Using Sieve of Eratosthenes to check for primality
    nums = n + 1
    is_prime = all(1 for num in range(2, nums) if num > 1 and n % num == 0)
    return is_prime
```