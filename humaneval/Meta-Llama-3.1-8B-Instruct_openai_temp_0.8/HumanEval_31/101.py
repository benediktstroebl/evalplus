```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.
    
    Args:
    n (int): The number to check for primality.
    
    Returns:
    bool: True if n is prime, False otherwise.
    """
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_divisor = int(n**0.5) + 1
    for d in range(3, max_divisor, 2):
        if n % d == 0:
            return False
    return True

# Example usage
print(is_prime(6))   # False
print(is_prime(101)) # True
print(is_prime(11))  # True
print(is_prime(13441)) # True
print(is_prime(61))  # True
print(is_prime(4))   # False
print(is_prime(1))   # False
```

This script defines a function `is_prime(n)` that checks whether a given integer `n` is prime or not. It first handles the edge cases where `n` is less than or equal to 1 (in which case it returns `False`), or `n` is 2 (in which case it returns `True`). It then checks whether `n` is divisible by any odd numbers up to the square root of `n`, and returns `False` if it finds any divisors. If it doesn't find any divisors, it returns `True`, indicating that `n` is prime. The example usage at the end demonstrates the function's behavior on the given test cases.