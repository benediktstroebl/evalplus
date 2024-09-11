### Prime Number Checker
```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.

    Parameters:
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
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_divisor = int(n**0.5) + 1
    for d in range(3, max_divisor, 2):
        if n % d == 0:
            return False
    return True

# Test the function
print(is_prime(6))      # False
print(is_prime(101))    # True
print(is_prime(11))     # True
print(is_prime(13441))  # True
print(is_prime(61))     # True
print(is_prime(4))      # False
print(is_prime(1))      # False
```
This script defines a function `is_prime` that checks whether a given integer `n` is prime. The function works by checking divisibility up to the square root of `n`, as any factor larger than that would have a corresponding factor smaller than the square root. If `n` is less than or equal to 1, it is not prime. If `n` is 2, it is prime. If `n` is even, it is not prime unless it is 2. Finally, the function checks divisibility by odd numbers up to the square root of `n`. If any divisor is found, the function returns `False`; otherwise, it returns `True`.