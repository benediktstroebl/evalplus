### Prime Number Check
#### Python Function to Determine if a Number is Prime
```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.
    
    A prime number is a positive integer that is divisible only by itself and 1.
    
    Parameters:
    n (int): The number to check for primality.
    
    Returns:
    bool: True if the number is prime, False otherwise.
    """
    # Handle edge cases where n is less than or equal to 1
    if n <= 1:
        return False
    
    # Check if n is divisible by any number up to its square root
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    
    # If n is not divisible by any number up to its square root, it's prime
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
This script defines a function `is_prime(n)` that checks if a given number `n` is prime. It uses a simple trial division method to check divisibility up to the square root of `n`, which is an optimized approach to reduce the number of iterations. The function returns `True` if `n` is prime and `False` otherwise. The test cases at the end demonstrate the function's correctness.