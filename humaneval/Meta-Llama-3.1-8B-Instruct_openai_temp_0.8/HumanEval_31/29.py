```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.

    Args:
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

# Test cases
print(is_prime(6))  # False
print(is_prime(101))  # True
print(is_prime(11))  # True
print(is_prime(13441))  # True
print(is_prime(61))  # True
print(is_prime(4))  # False
print(is_prime(1))  # False
```

This script defines a function `is_prime` that checks if a given number `n` is prime. It first handles the edge cases where `n` is less than or equal to 1 (not prime), or `n` is 2 (prime). Then, it checks if `n` is divisible by any odd number up to the square root of `n`. If `n` is divisible by any of these numbers, it is not prime. If `n` is not divisible by any of these numbers, it is prime. The script then tests the `is_prime` function with the provided test cases.