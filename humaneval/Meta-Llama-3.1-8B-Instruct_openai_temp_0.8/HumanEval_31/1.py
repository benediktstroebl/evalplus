```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.

    A prime number is a number that is divisible only by itself and 1.
    """
    # Edge cases: numbers less than 2 are not prime
    if n < 2:
        return False
    
    # Check divisibility up to the square root of n
    for i in range(2, int(n**0.5) + 1):
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

This script defines a function `is_prime(n)` that takes an integer `n` as input and returns `True` if `n` is prime and `False` otherwise. The function uses a simple trial division method to check for primality, which is sufficient for small to medium-sized numbers.