```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.
    
    A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

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
    elif n <= 3:
        # 2 and 3 are prime
        return True
    elif n % 2 == 0 or n % 3 == 0:
        # Numbers that are divisible by 2 or 3 are not prime
        return False
    i = 5
    while i * i <= n:
        # Check for divisibility up to the square root of n
        if n % i == 0 or n % (i + 2) == 0:
            # If n is divisible by i or i+2, it's not prime
            return False
        i += 6
    return True

# Test the function
print(is_prime(6))    # False
print(is_prime(101))  # True
print(is_prime(11))   # True
print(is_prime(13441))# True
print(is_prime(61))   # True
print(is_prime(4))    # False
print(is_prime(1))    # False
```

This script implements the `is_prime` function according to the problem statement. The function uses a simple trial division approach to check for primality, which is sufficient for small to medium-sized numbers. It first checks for numbers less than or equal to 1, then for 2 and 3 (which are prime), and finally checks for divisibility up to the square root of the number. If the number is divisible by any of these values, it's not prime. Otherwise, it's prime. The script includes test cases to verify the correctness of the function.