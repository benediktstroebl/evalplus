```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.

    Args:
        n (int): The number to check for primality.

    Returns:
        bool: True if the number is prime, False otherwise.
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
print(is_prime(6))  # False
print(is_prime(101))  # True
print(is_prime(11))  # True
print(is_prime(13441))  # True
print(is_prime(61))  # True
print(is_prime(4))  # False
print(is_prime(1))  # False
```

This script defines a function `is_prime(n)` that takes an integer `n` as input and returns `True` if `n` is prime and `False` otherwise. The function works by checking if `n` is divisible by any number up to its square root, as any factor larger than the square root would have a corresponding factor smaller than the square root. The test cases at the end of the script demonstrate the function's correctness.