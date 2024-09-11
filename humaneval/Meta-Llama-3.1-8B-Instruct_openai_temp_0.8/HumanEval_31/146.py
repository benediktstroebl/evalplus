```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.

    A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

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
    if n <= 1:  # Numbers less than or equal to 1 are not prime
        return False
    if n <= 3:  # 2 and 3 are prime
        return True
    if n % 2 == 0 or n % 3 == 0:  # If n is divisible by 2 or 3, it's not prime
        return False
    i = 5
    while i * i <= n:  # We only need to check up to the square root of n
        if n % i == 0 or n % (i + 2) == 0:  # Check for divisibility by 6k +/- 1
            return False
        i += 6
    return True
```

This implementation uses a simple trial division method to check for primality. It first handles the special cases where n is less than or equal to 1, 2, or 3. Then it checks if n is divisible by 2 or 3, and if so, it's not prime. Otherwise, it checks for divisibility by 6k +/- 1 up to the square root of n, using a loop that increments by 6 each time. If n is not divisible by any of these numbers, it's prime.