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
    bool: True if n is prime, False otherwise.
    """
    if n <= 1:  # Numbers less than or equal to 1 are not prime
        return False
    elif n <= 3:  # 2 and 3 are prime
        return True
    elif n % 2 == 0 or n % 3 == 0:  # If n is divisible by 2 or 3, it's not prime
        return False
    i = 5
    while i * i <= n:  # Only need to check up to the square root of n
        if n % i == 0 or n % (i + 2) == 0:  # Check for divisibility by i and i + 2
            return False
        i += 6  # Increment by 6 to check the next pair of potential divisors
    return True

# Example usage:
print(is_prime(6))      # False
print(is_prime(101))    # True
print(is_prime(11))     # True
print(is_prime(13441))  # True
print(is_prime(61))     # True
print(is_prime(4))      # False
print(is_prime(1))      # False
```

This script defines a function `is_prime(n)` that checks if a given number `n` is prime. It uses a simple trial division method, which is efficient for small numbers. The function returns `True` if `n` is prime and `False` otherwise. The example usage at the end shows how to use the function to check various numbers for primality.