```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.

    A prime number is a positive integer greater than 1 that has no positive integer divisors other than 1 and itself.

    Args:
        n (int): The number to check for primality.

    Returns:
        bool: True if the number is prime, False otherwise.

    Examples:
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
    # Edge cases: numbers less than 2 are not prime
    if n < 2:
        return False

    # Check divisibility from 2 to the square root of n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    # If no divisors are found, the number is prime
    return True

# Test the function
if __name__ == "__main__":
    import doctest
    doctest.testmod()
```

This script defines a function `is_prime` that checks whether a given number `n` is prime or not. It uses a simple trial division method to check divisibility up to the square root of `n`. If `n` is less than 2, it immediately returns `False`. The script also includes a test suite using the `doctest` module to ensure the function behaves as expected.