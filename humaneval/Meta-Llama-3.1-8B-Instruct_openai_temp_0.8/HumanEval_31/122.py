### Prime Number Checker
#### A Python Script to Determine if a Number is Prime

```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.
    
    A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
    
    Parameters:
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

### Example Usage:

print(is_prime(6))  # False
print(is_prime(101))  # True
print(is_prime(11))  # True
print(is_prime(13441))  # True
print(is_prime(61))  # True
print(is_prime(4))  # False
print(is_prime(1))  # False
```

This script defines a function `is_prime(n)` that takes an integer `n` as input and returns `True` if `n` is prime, and `False` otherwise. The function uses a simple trial division method to check for primality, which is efficient for small to medium-sized numbers. For larger numbers, more advanced primality tests such as the Miller-Rabin test may be necessary.