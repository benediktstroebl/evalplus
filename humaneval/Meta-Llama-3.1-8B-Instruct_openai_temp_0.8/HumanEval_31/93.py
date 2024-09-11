```python
# Function to check if a number is prime
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.

    Parameters:
    n (int): The number to be checked.

    Returns:
    bool: True if the number is prime, False otherwise.
    """
    
    # Corner cases: numbers less than 2 are not prime
    if n < 2:
        return False
    
    # Check from 2 to the square root of n
    for i in range(2, int(n**0.5) + 1):
        # If n is divisible by any number between 2 and its square root, it's not prime
        if n % i == 0:
            return False
    
    # If n is not divisible by any number between 2 and its square root, it's prime
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

This script defines a function `is_prime(n)` that checks whether a given number `n` is prime or not. It returns `True` if `n` is prime and `False` otherwise. The function checks for divisibility from 2 to the square root of `n`, which is a more efficient approach than checking up to `n-1`. The script also includes test cases to verify the correctness of the function.