### Prime Number Checker
#### Python Implementation

```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.

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
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_divisor = int(n**0.5) + 1
    for d in range(3, max_divisor, 2):
        if n % d == 0:
            return False
    return True

# Test cases
print(is_prime(6))     # False
print(is_prime(101))   # True
print(is_prime(11))    # True
print(is_prime(13441)) # True
print(is_prime(61))    # True
print(is_prime(4))     # False
print(is_prime(1))     # False
```

This script defines a function `is_prime(n)` that checks whether a given number `n` is prime. It returns `True` if the number is prime and `False` otherwise.

The function first handles the base cases where `n` is less than or equal to 1 (not prime), `n` is 2 (prime), or `n` is even (not prime).

For odd numbers greater than 2, it checks divisibility up to the square root of `n` (rounded up to the nearest integer) to optimize the search. If `n` is divisible by any of these numbers, it is not prime.

Finally, if `n` is not divisible by any of the numbers checked, it is prime, and the function returns `True`.