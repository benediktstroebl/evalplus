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
    # We only need to check divisors up to the square root of n
    for d in range(3, max_divisor, 2):
        # Check if n is divisible by any odd number up to the square root
        if n % d == 0:
            return False
    return True

# Test the function
print(is_prime(6))   # False
print(is_prime(101)) # True
print(is_prime(11))  # True
print(is_prime(13441)) # True
print(is_prime(61))  # True
print(is_prime(4))   # False
print(is_prime(1))   # False
```

This script defines a function `is_prime(n)` that checks if a given number `n` is prime. It returns `True` if the number is prime and `False` otherwise. The function uses the following optimizations:

1. Numbers less than or equal to 1 are not prime.
2. 2 is the only even prime number, so we can immediately return `True` if `n` is 2.
3. All other even numbers are not prime, so we can immediately return `False` if `n` is even.
4. We only need to check divisors up to the square root of `n`, so we use a loop to check odd numbers up to the square root of `n`.