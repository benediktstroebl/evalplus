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
        # Numbers less than or equal to 1 are not prime
        return False
    elif n <= 3:
        # 2 and 3 are prime
        return True
    elif n % 2 == 0 or n % 3 == 0:
        # If the number is divisible by 2 or 3, it's not prime
        return False
    i = 5
    while i * i <= n:
        # Check for divisibility up to the square root of n
        if n % i == 0 or n % (i + 2) == 0:
            # If the number is divisible by any odd number, it's not prime
            return False
        i += 6
    return True

# Test cases
print(is_prime(6))  # False
print(is_prime(101))  # True
print(is_prime(11))  # True
print(is_prime(13441))  # True
print(is_prime(61))  # True
print(is_prime(4))  # False
print(is_prime(1))  # False
```

This script defines a function `is_prime` that takes an integer `n` as input and returns `True` if `n` is prime and `False` otherwise. The function uses a loop to check for divisibility up to the square root of `n`, which is a common optimization for primality testing. The script includes the original test cases as comments to verify the correctness of the implementation.