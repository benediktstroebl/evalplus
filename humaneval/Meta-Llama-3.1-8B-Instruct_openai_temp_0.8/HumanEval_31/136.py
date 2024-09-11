```python
def is_prime(n):
    """Return true if a given number is prime, and false otherwise.

    Args:
        n (int): The number to check for primality.

    Returns:
        bool: True if n is prime, False otherwise.
    """
    if n <= 1:  # 1 and numbers less than 1 are not prime
        return False
    if n == 2:  # 2 is the only even prime number
        return True
    if n % 2 == 0:  # All other even numbers are not prime
        return False
    max_divisor = int(n**0.5) + 1  # Only need to check up to the square root of n
    for d in range(3, max_divisor, 2):  # Only need to check odd numbers
        if n % d == 0:  # If n is divisible by any number, it's not prime
            return False
    return True

# Test cases
print(is_prime(6))      # False
print(is_prime(101))    # True
print(is_prime(11))     # True
print(is_prime(13441))  # True
print(is_prime(61))     # True
print(is_prime(4))      # False
print(is_prime(1))      # False
```

This script defines a function `is_prime(n)` that checks whether a given number `n` is prime. It uses the following criteria to determine primality:

- Numbers less than or equal to 1 are not prime.
- 2 is the only even prime number.
- All other even numbers are not prime.
- Only need to check odd numbers up to the square root of `n` for divisors.

The script then includes the provided test cases to demonstrate the function's correctness.