### Prime Number Checker
Below is a Python script that defines a function `is_prime(n)` to check if a given number `n` is prime.

```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.

    Args:
        n (int): The number to check for primality.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if n <= 1:  # Numbers less than or equal to 1 are not prime
        return False
    for i in range(2, int(n ** 0.5) + 1):  # Check divisibility up to the square root of n
        if n % i == 0:  # If n is divisible by any number, it's not prime
            return False
    return True  # If n is not divisible by any number, it's prime

# Test cases
print(is_prime(6))  # False
print(is_prime(101))  # True
print(is_prime(11))  # True
print(is_prime(13441))  # True
print(is_prime(61))  # True
print(is_prime(4))  # False
print(is_prime(1))  # False
```

This script uses the following approach to check for primality:

1. First, we check if `n` is less than or equal to 1, in which case it's not prime.
2. Next, we loop from 2 to the square root of `n` (inclusive) and check if `n` is divisible by any of these numbers.
3. If `n` is divisible by any number, we immediately return `False`.
4. If we reach the loop without finding a divisor, we return `True`, indicating that `n` is prime.