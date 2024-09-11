```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.

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
    if n <= 1:  # Numbers less than or equal to 1 are not prime
        return False
    for i in range(2, int(n**0.5) + 1):  # Only need to check up to sqrt(n)
        if n % i == 0:  # If n is divisible by any number between 2 and sqrt(n)
            return False
    return True  # If n is not divisible by any number between 2 and sqrt(n), it's prime


# Test cases
print(is_prime(6))   # False
print(is_prime(101)) # True
print(is_prime(11))  # True
print(is_prime(13441)) # True
print(is_prime(61))  # True
print(is_prime(4))   # False
print(is_prime(1))   # False
```

This script defines a function `is_prime(n)` that checks whether a given number `n` is prime or not. It then tests this function with the provided examples. The function uses a simple trial division method to check for primality, which is sufficient for small to medium-sized numbers. For larger numbers, a more efficient algorithm such as the Miller-Rabin primality test may be needed.