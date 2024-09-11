### Prime Number Checker
#### A Python Function to Determine if a Given Number is Prime

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
    if n <= 1:  # 0 and 1 are not prime numbers
        return False
    for i in range(2, int(n ** 0.5) + 1):  # only need to check up to square root of n
        if n % i == 0:  # if n is divisible by i, it's not prime
            return False
    return True  # if no divisors found, n is prime

# Example usage:
print(is_prime(6))   # False
print(is_prime(101)) # True
print(is_prime(11))  # True
print(is_prime(13441))# True
print(is_prime(61))  # True
print(is_prime(4))   # False
print(is_prime(1))   # False
```

This script defines a function `is_prime(n)` that takes an integer `n` as input and returns `True` if it's a prime number, and `False` otherwise. The function uses a simple trial division method to check for primality, and it only needs to check up to the square root of `n` (rounded up to the nearest integer), which makes the function more efficient for larger inputs. The example usage at the end demonstrates how to use the function with different inputs.