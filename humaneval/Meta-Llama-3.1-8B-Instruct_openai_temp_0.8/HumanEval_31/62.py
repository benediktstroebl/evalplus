### Prime Number Checker in Python

#### Code

```markdown
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.
    
    Args:
        n (int): The number to check.
    
    Returns:
        bool: Whether the number is prime.
    """
    if n <= 1:
        # Prime numbers are greater than 1
        return False
    for i in range(2, int(n ** 0.5) + 1):
        # Check if n is divisible by any number from 2 to sqrt(n)
        if n % i == 0:
            return False
    return True

# Test cases
print(is_prime(6))   # False
print(is_prime(101)) # True
print(is_prime(11))  # True
print(is_prime(13441)) # True
print(is_prime(61))  # True
print(is_prime(4))   # False
print(is_prime(1))   # False
```

#### Explanation

This Python function `is_prime(n)` checks whether a given number `n` is prime. It does this by iterating from 2 to the square root of `n` and checking if `n` is divisible by any of these numbers. If it is, then `n` is not prime and the function returns `False`. Otherwise, the function returns `True`.

The reason we only need to check up to the square root of `n` is that a larger factor of `n` must be a multiple of a smaller factor that has already been checked.