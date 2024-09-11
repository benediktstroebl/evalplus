```python
def is_prime(n):
    """Return true if a given number is prime, and false otherwise.

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
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Test the function
print(is_prime(6))    # False
print(is_prime(101))  # True
print(is_prime(11))   # True
print(is_prime(13441)) # True
print(is_prime(61))   # True
print(is_prime(4))    # False
print(is_prime(1))    # False
```

This script defines a function `is_prime(n)` that checks whether a given number `n` is prime or not. It uses a basic trial division method to check for primality. The function first handles the edge cases where `n` is less than or equal to 1 or 3. If `n` is divisible by 2 or 3, it's not prime. Otherwise, it checks divisibility up to the square root of `n` using increments of 6 (since all primes are of the form 6k ± 1). If `n` passes these checks, it's prime.