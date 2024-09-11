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
        return False  # 1 and numbers less than 1 are not prime
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False  # If n is divisible by any number between 2 and sqrt(n), it's not prime
    return True  # If n is not divisible by any of the above numbers, it's prime


# Test cases
print(is_prime(6))   # False
print(is_prime(101)) # True
print(is_prime(11))  # True
print(is_prime(13441)) # True
print(is_prime(61))  # True
print(is_prime(4))   # False
print(is_prime(1))   # False
```

This script defines a function `is_prime(n)` that checks whether a given number `n` is prime or not. It does this by checking divisibility of `n` by all numbers up to its square root. If `n` is divisible by any of these numbers, it's not prime. If it's not divisible by any of them, it's prime. The script then includes some test cases to demonstrate its functionality.