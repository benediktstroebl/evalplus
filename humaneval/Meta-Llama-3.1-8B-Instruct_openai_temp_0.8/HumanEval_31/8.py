Here's a Python script that implements the `is_prime` function:

```markdown
# is_prime function implementation
=====================================

This script defines a function `is_prime(n)` that checks if a given number is prime.

```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.
    
    Args:
        n (int): The number to be checked for primality.
    
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
    
    # Check if the number is divisible by any number up to its square root
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    
    # If the number is not divisible by any number up to its square root, it's prime
    return True
```

### Example Use Cases

```python
# Test the is_prime function with some examples
print(is_prime(6))  # Output: False
print(is_prime(101))  # Output: True
print(is_prime(11))  # Output: True
print(is_prime(13441))  # Output: True
print(is_prime(61))  # Output: True
print(is_prime(4))  # Output: False
print(is_prime(1))  # Output: False
```

This script uses a simple trial division method to check if a number is prime. It only checks divisibility up to the square root of the number, which is sufficient because a larger factor of the number would be a multiple of a smaller factor that has already been checked.