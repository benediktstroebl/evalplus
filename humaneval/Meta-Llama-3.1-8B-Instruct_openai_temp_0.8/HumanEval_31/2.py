### Prime Number Checker in Python
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

# Example usage:
print(is_prime(6))   # False
print(is_prime(101)) # True
print(is_prime(11))  # True
print(is_prime(13441)) # True
print(is_prime(61))  # True
print(is_prime(4))   # False
print(is_prime(1))   # False
```
This script defines a function `is_prime` that checks whether a given number `n` is prime. It uses a few optimizations:

- Numbers less than or equal to 1 are not prime.
- 2 is the only even prime number.
- If `n` is even and not 2, it's not prime.
- We only need to check divisors up to the square root of `n`, as any factor larger than that would have a corresponding factor smaller than the square root.

This approach makes the function more efficient for larger inputs.