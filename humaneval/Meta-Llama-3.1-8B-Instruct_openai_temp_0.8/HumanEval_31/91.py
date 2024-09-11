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
    # Corner cases: numbers less than 2 are not prime
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2:
        return True
    # All other even numbers are not prime
    if n % 2 == 0:
        return False
    # Check odd factors up to the square root of n
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    # If no factors were found, the number is prime
    return True


# Test cases
if __name__ == "__main__":
    assert not is_prime(6)
    assert is_prime(101)
    assert is_prime(11)
    assert is_prime(13441)
    assert is_prime(61)
    assert not is_prime(4)
    assert not is_prime(1)
```

This script defines a function `is_prime(n)` that checks if a given number `n` is prime. It uses a simple trial division method to check for factors, which is sufficient for small to medium-sized integers. The function is then tested with the provided test cases.