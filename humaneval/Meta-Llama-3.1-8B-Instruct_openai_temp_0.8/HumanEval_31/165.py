### Prime Number Checker
Below is a Python function that checks whether a given number is prime or not.

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
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Example usage:
print(is_prime(6))   # Output: False
print(is_prime(101)) # Output: True
print(is_prime(11))  # Output: True
print(is_prime(13441))  # Output: True
print(is_prime(61))  # Output: True
print(is_prime(4))   # Output: False
print(is_prime(1))   # Output: False
```

In this code, we're using a simple trial division method to check for primality. We only need to check divisors up to the square root of the number, as any factor larger than that would have a corresponding factor smaller than the square root. This makes the function more efficient for larger numbers.