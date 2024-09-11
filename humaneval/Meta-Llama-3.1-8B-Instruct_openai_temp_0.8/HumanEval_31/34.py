```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.
    
    A prime number is a positive integer greater than 1 that has no positive divisors other than 1 and itself.
    
    Args:
        n (int): The number to check for primality.
    
    Returns:
        bool: True if n is prime, False otherwise.
    """
    if n <= 1:  # numbers less than or equal to 1 are not prime
        return False
    for i in range(2, int(n**0.5) + 1):  # only need to check up to the square root of n
        if n % i == 0:  # if n is divisible by any number between 2 and its square root, it's not prime
            return False
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

This script defines a function `is_prime(n)` that checks whether a given integer `n` is prime. It returns `True` if `n` is prime and `False` otherwise. The function uses a loop to check for divisibility up to the square root of `n`, which is an optimization to reduce the number of iterations. The test cases at the end of the script demonstrate the function's behavior.