### Prime Number Checker
#### Python Script

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
        # Numbers less than or equal to 1 are not prime.
        return False
    elif n <= 3:
        # 2 and 3 are prime numbers.
        return True
    elif n % 2 == 0 or n % 3 == 0:
        # If the number is divisible by 2 or 3, it's not prime.
        return False
    i = 5
    while i * i <= n:
        # We only need to check up to the square root of n.
        if n % i == 0 or n % (i + 2) == 0:
            # If the number is divisible by any of these values, it's not prime.
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

This script defines a function `is_prime(n)` that checks if a given number `n` is prime. It uses a simple trial division method, which is efficient for small to medium-sized numbers. The test cases at the end demonstrate the function's correctness.