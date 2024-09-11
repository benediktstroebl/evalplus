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
    if n <= 1:  # edge case: numbers less than or equal to 1 are not prime
        return False
    if n == 2:  # edge case: 2 is the only even prime number
        return True
    if n % 2 == 0:  # if the number is even, it's not prime
        return False
    max_divisor = int(n**0.5) + 1  # only need to check up to the square root of n
    for d in range(3, max_divisor, 2):  # only need to check odd numbers
        if n % d == 0:
            return False
    return True  # if no divisors are found, the number is prime

# Example usage:
print(is_prime(6))  # False
print(is_prime(101))  # True
print(is_prime(11))  # True
print(is_prime(13441))  # True
print(is_prime(61))  # True
print(is_prime(4))  # False
print(is_prime(1))  # False
```

This script defines the `is_prime` function, which checks whether a given integer `n` is prime. It uses a combination of edge cases and a loop to check for divisors up to the square root of `n`. The function returns `True` if `n` is prime and `False` otherwise. The script also includes example usage to demonstrate the function's behavior.