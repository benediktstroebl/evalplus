```python
def is_prime(n):
    """Return true if a given number is prime, and false otherwise.

    Args:
        n (int): The number to check for primality.

    Returns:
        bool: True if n is prime, False otherwise.

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

# Test the function
print(is_prime(6))   # False
print(is_prime(101)) # True
print(is_prime(11))  # True
print(is_prime(13441)) # True
print(is_prime(61))  # True
print(is_prime(4))   # False
print(is_prime(1))   # False
```

This script defines a function `is_prime` that takes an integer `n` as input and returns a boolean value indicating whether `n` is prime or not. The function works by checking if `n` is less than or equal to 1 (in which case it's not prime), if `n` is 2 (the only even prime number), if `n` is divisible by 2 (in which case it's not prime), or if `n` has any divisors between 3 and the square root of `n` (inclusive). If `n` passes all these checks, it's prime.