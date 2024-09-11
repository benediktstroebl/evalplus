### Prime Number Checker

Below is a Python function that checks if a given number is prime.

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
    for i in range(2, int(n**0.5) + 1):
        # Check for divisibility up to the square root of n
        if n % i == 0:
            # If n is divisible by any number, it's not prime
            return False
    # If n is not divisible by any number, it's prime
    return True

# Test cases
print(is_prime(6))      # False
print(is_prime(101))    # True
print(is_prime(11))     # True
print(is_prime(13441))  # True
print(is_prime(61))     # True
print(is_prime(4))      # False
print(is_prime(1))      # False
```

This function works by checking whether the input number `n` is divisible by any number up to its square root. If `n` is divisible by any of these numbers, it's not prime. Otherwise, it's prime. This function has a time complexity of O(√n), making it efficient for large numbers.