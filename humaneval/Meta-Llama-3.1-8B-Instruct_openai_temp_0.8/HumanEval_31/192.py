```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.

    A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
    
    Args:
        n (int): The number to check.

    Returns:
        bool: True if n is prime, False otherwise.
    """
    if n <= 1:  # 1 and numbers less than 1 are not prime
        return False
    for i in range(2, int(n**0.5) + 1):  # check from 2 to sqrt(n)
        if n % i == 0:  # if n is divisible by i, it's not prime
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

This script defines a function `is_prime(n)` that takes an integer `n` as input and returns `True` if `n` is prime and `False` otherwise. The function checks divisibility of `n` by all numbers from 2 to the square root of `n`, and returns `False` as soon as it finds a divisor. If `n` is not divisible by any of these numbers, it is prime, and the function returns `True`. The script also includes test cases to demonstrate the function's behavior.