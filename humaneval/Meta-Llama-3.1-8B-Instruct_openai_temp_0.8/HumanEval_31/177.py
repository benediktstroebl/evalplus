### Prime Number Checker
The provided function checks whether a given number is prime or not.

#### Code

```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.
    
    Parameters:
    n (int): The number to check for primality.
    
    Returns:
    bool: True if n is prime, False otherwise.
    """
    
    # Handle edge cases
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    # Check for factors up to the square root of n
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    
    return True

# Example usage
if __name__ == "__main__":
    print(is_prime(6))       # False
    print(is_prime(101))     # True
    print(is_prime(11))      # True
    print(is_prime(13441))   # True
    print(is_prime(61))      # True
    print(is_prime(4))       # False
    print(is_prime(1))       # False
```

This script defines a function `is_prime(n)` that checks whether the given number `n` is prime or not. It handles edge cases, checks for factors up to the square root of `n`, and returns `True` if `n` is prime and `False` otherwise. The example usage demonstrates how to call the function and verify its correctness with the provided test cases.