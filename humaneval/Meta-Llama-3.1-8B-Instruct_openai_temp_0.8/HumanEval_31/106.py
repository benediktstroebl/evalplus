```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if the number is prime, false otherwise.
    """
    if n <= 1:  # 0 and 1 are not prime numbers
        return False
    for i in range(2, int(n**0.5) + 1):  # Only need to check up to the square root of n
        if n % i == 0:  # If n is divisible by any number between 2 and its square root, it's not prime
            return False
    return True


# Test cases
print(is_prime(6))   # False
print(is_prime(101)) # True
print(is_prime(11))  # True
print(is_prime(13441))  # True
print(is_prime(61))   # True
print(is_prime(4))    # False
print(is_prime(1))    # False
```

This script defines a function `is_prime(n)` that checks whether a given number `n` is prime or not. It returns `True` if `n` is prime and `False` otherwise. The function first checks if `n` is less than or equal to 1, in which case it returns `False` since 0 and 1 are not prime numbers. Then it checks divisibility of `n` by all numbers from 2 to its square root (inclusive), and if `n` is divisible by any of these numbers, it returns `False`. If `n` is not divisible by any of these numbers, it returns `True`. The test cases at the end of the script demonstrate the function's usage.