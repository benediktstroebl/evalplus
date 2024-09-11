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
        # 1 and numbers less than 1 are not prime
        return False
    if n <= 3:
        # 2 and 3 are prime
        return True
    if n % 2 == 0 or n % 3 == 0:
        # If the number is divisible by 2 or 3, it's not prime
        return False
    i = 5
    while i * i <= n:
        # Check if the number is divisible by any odd number up to its square root
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Example usage:
print(is_prime(6))  # Output: False
print(is_prime(101))  # Output: True
print(is_prime(11))  # Output: True
print(is_prime(13441))  # Output: True
print(is_prime(61))  # Output: True
print(is_prime(4))  # Output: False
print(is_prime(1))  # Output: False
```

This script defines a function `is_prime(n)` that takes an integer `n` as input and returns a boolean indicating whether `n` is prime or not. The function uses a combination of simple primality tests and a divisibility check to efficiently determine whether `n` is prime. It also includes example usage and documentation comments to illustrate the function's behavior.