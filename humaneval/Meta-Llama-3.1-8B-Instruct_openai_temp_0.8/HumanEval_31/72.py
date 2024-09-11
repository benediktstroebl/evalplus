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
    if n <= 1:  # 1 and numbers less than 1 are not prime
        return False
    if n == 2:  # 2 is the only even prime number
        return True
    if n % 2 == 0:  # All other even numbers are not prime
        return False
    max_divisor = int(n**0.5) + 1  # Only need to check up to the square root of n
    for d in range(3, max_divisor, 2):  # Check odd numbers up to the square root of n
        if n % d == 0:
            return False
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

This script defines a function `is_prime(n)` that checks if a given number `n` is prime. The function uses a series of conditions to optimize the primality test:

1.  If `n` is less than or equal to 1, it is not prime.
2.  If `n` is 2, it is prime.
3.  If `n` is even (i.e., `n % 2 == 0`), it is not prime.
4.  Otherwise, check odd numbers up to the square root of `n` to see if they divide `n` evenly. If any do, `n` is not prime.

The script includes detailed documentation and test cases to demonstrate the function's behavior.