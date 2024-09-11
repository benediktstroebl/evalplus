### Prime Number Checker
#### Function: `is_prime(n)`

```python
def is_prime(n):
    """
    Return True if a given number is prime, and False otherwise.

    A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
    
    Example use cases:
    >>> is_prime(6)
    False
    >>> is_prime(101)
    True
    >>> is_prime(11)
    True
    >>> is_prime(13441)
    True
    >>> is_prime(61)
    True
    >>> is_prime(4)
    False
    >>> is_prime(1)
    False
    """

    # Corner cases: numbers less than 2 are not prime
    if n < 2:
        return False

    # Check divisibility up to the square root of n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    # If no divisors are found, the number is prime
    return True
```

This function uses a simple iterative approach to check if a given number `n` is prime. It first checks for corner cases (numbers less than 2) and then iterates from 2 up to the square root of `n`. If any divisor is found within this range, the function immediately returns `False`, indicating that `n` is not prime. If no divisors are found, the function returns `True`, indicating that `n` is prime.