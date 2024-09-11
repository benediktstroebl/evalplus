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
    if n == 2:
        # 2 is the only even prime number
        return True
    if n % 2 == 0:
        # All other even numbers are not prime
        return False
    max_divisor = int(n**0.5) + 1
    # Check odd divisors up to the square root of n
    for d in range(3, max_divisor, 2):
        if n % d == 0:
            # If n has an odd divisor, it's not prime
            return False
    # If n has no odd divisors, it's prime
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

This script defines a function `is_prime(n)` that checks whether a given integer `n` is prime or not. It uses a simple trial division method to check for primality. The function first checks for some special cases (numbers less than or equal to 1, the number 2, and even numbers), then checks odd divisors up to the square root of `n`.