### Prime Number Checker
#### A Python Script

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
    if n <= 1:  # Numbers less than or equal to 1 are not prime
        return False
    
    for i in range(2, int(n ** 0.5) + 1):  # Only need to check up to the square root of n
        if n % i == 0:  # If n is divisible by i, it's not a prime number
            return False
    
    return True  # If no divisors are found, the number is prime


# Test cases
print(is_prime(6))   # False
print(is_prime(101)) # True
print(is_prime(11))  # True
print(is_prime(13441)) # True
print(is_prime(61))  # True
print(is_prime(4))   # False
print(is_prime(1))   # False
```

This script defines a function `is_prime(n)` that checks if a given number `n` is prime. It uses a simple trial division method to check for primality, which is sufficient for small numbers. For larger numbers, more advanced algorithms like the Miller-Rabin test would be needed. 

The script includes test cases to verify the correctness of the `is_prime(n)` function.