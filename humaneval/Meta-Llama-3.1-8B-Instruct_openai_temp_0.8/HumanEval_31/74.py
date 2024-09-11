### Prime Number Checker
```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.

    Args:
        n (int): The number to check.

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
    if n <= 1:  # Numbers less than or equal to 1 are not prime
        return False
    for i in range(2, int(n ** 0.5) + 1):  # Only check up to the square root
        if n % i == 0:  # If the number is divisible by any number, it's not prime
            return False
    return True  # If the number is not divisible by any number, it's prime

# Test cases
print(is_prime(6))  # False
print(is_prime(101))  # True
print(is_prime(11))  # True
print(is_prime(13441))  # True
print(is_prime(61))  # True
print(is_prime(4))  # False
print(is_prime(1))  # False
```
This script uses a simple trial division method to check if a number is prime. It checks divisibility up to the square root of the number, as any factor larger than that would have a corresponding factor smaller than the square root. If the number is divisible by any of these values, it's not prime. Otherwise, it's prime.