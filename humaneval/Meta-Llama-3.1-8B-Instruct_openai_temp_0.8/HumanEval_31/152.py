```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.

    A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

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
        return False  # Numbers less than or equal to 1 are not prime

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False  # If n is divisible by any number between 2 and sqrt(n), it's not prime

    return True  # If n is not divisible by any number, it's prime


# Test the function with the provided examples
print(is_prime(6))    # False
print(is_prime(101))  # True
print(is_prime(11))   # True
print(is_prime(13441))# True
print(is_prime(61))   # True
print(is_prime(4))    # False
print(is_prime(1))    # False
```

This script defines the `is_prime` function, which checks whether a given number `n` is prime. It uses a simple trial division method, checking divisibility up to the square root of `n`. If `n` is divisible by any number between 2 and its square root, it's not prime. Otherwise, it's prime. The function is then tested with the provided examples.