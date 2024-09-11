### Prime Number Checker
```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if n <= 1:
        # Numbers less than or equal to 1 are not prime
        return False
    if n <= 3:
        # 2 and 3 are prime
        return True
    if n % 2 == 0 or n % 3 == 0:
        # If the number is divisible by 2 or 3, it's not prime
        return False
    i = 5
    while i * i <= n:
        # Check divisibility up to the square root of n
        if n % i == 0 or n % (i + 2) == 0:
            # If the number is divisible by any odd number, it's not prime
            return False
        i += 6
    # If the number is not divisible by any of the above, it's prime
    return True

# Test cases
if __name__ == "__main__":
    print(is_prime(6))       # False
    print(is_prime(101))     # True
    print(is_prime(11))      # True
    print(is_prime(13441))   # True
    print(is_prime(61))      # True
    print(is_prime(4))       # False
    print(is_prime(1))       # False
```

This script defines a function `is_prime(n)` that checks whether a given number `n` is prime or not. It uses an optimized approach to reduce the number of checks required. The function returns `True` if the number is prime and `False` otherwise. The test cases at the end verify the function's correctness.