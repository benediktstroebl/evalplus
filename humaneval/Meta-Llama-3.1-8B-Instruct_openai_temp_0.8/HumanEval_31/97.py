### Prime Number Checker

```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.
    
    Parameters:
    n (int): The number to check for primality.
    
    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if n <= 1:
        # 0 and 1 are not prime numbers
        return False
    for i in range(2, int(n**0.5) + 1):
        # Check if n is divisible by any number up to its square root
        if n % i == 0:
            # If n is divisible, it's not a prime number
            return False
    # If n is not divisible by any number up to its square root, it's prime
    return True

# Example usage:
print(is_prime(6))  # False
print(is_prime(101))  # True
print(is_prime(11))  # True
print(is_prime(13441))  # True
print(is_prime(61))  # True
print(is_prime(4))  # False
print(is_prime(1))  # False
```

This script defines a function `is_prime(n)` that checks whether a given number `n` is prime or not. The function returns `True` if `n` is prime and `False` otherwise. The example usage at the end demonstrates the function's behavior with different inputs.