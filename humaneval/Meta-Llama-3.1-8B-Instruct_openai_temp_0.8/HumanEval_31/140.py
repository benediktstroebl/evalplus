### Python Prime Number Checker
```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.

    Args:
    n (int): The number to check for primality.

    Returns:
    bool: True if n is prime, False otherwise.
    """
    if n <= 1:  # 1 and numbers less than 1 are not prime
        return False
    for i in range(2, int(n**0.5) + 1):  # only check up to the square root of n
        if n % i == 0:  # if n is divisible by any number, it's not prime
            return False
    return True  # if n is not divisible by any number, it's prime

# Test cases
print(is_prime(6))  # False
print(is_prime(101))  # True
print(is_prime(11))  # True
print(is_prime(13441))  # True
print(is_prime(61))  # True
print(is_prime(4))  # False
print(is_prime(1))  # False
```

This script defines a function `is_prime(n)` that checks if a given number `n` is prime. The function returns `False` if `n` is less than or equal to 1, as these numbers are not prime. Otherwise, it checks divisibility up to the square root of `n` (since a larger factor of `n` must be a multiple of a smaller factor that has already been checked). If `n` is divisible by any number, it's not prime; otherwise, it's prime.

The test cases provided in the original problem are used to verify the correctness of the `is_prime(n)` function.