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
        # Numbers less than or equal to 1 are not prime
        return False
    if n == 2:
        # 2 is the only even prime number
        return True
    if n % 2 == 0:
        # Even numbers greater than 2 are not prime
        return False
    # Check divisibility up to the square root of the number
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            # If the number is divisible, it's not prime
            return False
    # If the number is not divisible by any of the above, it's prime
    return True

# Example usage:
print(is_prime(6))  # False
print(is_prime(101))  # True
print(is_prime(11))  # True
print(is_prime(13441))  # True
print(is_prime(61))  # True
print(is_prime(4))  # False
print(is_prime(1))  # False
```

This script defines a function `is_prime(n)` that takes an integer `n` as input and returns a boolean value indicating whether the number is prime or not. It uses a simple trial division method to check for primality, which is sufficient for small to medium-sized integers. For larger integers, a more advanced primality test such as the Miller-Rabin test may be necessary.