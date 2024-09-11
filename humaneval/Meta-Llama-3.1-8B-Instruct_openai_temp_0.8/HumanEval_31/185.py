### Primality Check Function
```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.

    Args:
    n (int): The number to check for primality.

    Returns:
    bool: True if n is prime, False otherwise.
    """
    # Corner cases: Numbers less than 2 are not prime
    if n < 2:
        return False

    # Check from 2 to the square root of n
    # We only need to check up to the square root because a larger factor of n would be a multiple of a smaller factor that has already been checked
    for i in range(2, int(n ** 0.5) + 1):
        # If n is divisible by i, it's not prime
        if n % i == 0:
            return False

    # If we've checked all numbers and haven't found a divisor, n is prime
    return True

# Example usage:
print(is_prime(6))  # False
print(is_prime(101))  # True
print(is_prime(11))  # True
print(is_prime(13441))  # True
print(is_prime(61))  # True
print(is_prime(4))  # False
print(is_prime(1))  # False
```
This script defines a function `is_prime(n)` that checks if a given number `n` is prime. It handles corner cases (numbers less than 2) and checks for divisibility up to the square root of `n`. The function returns `True` if `n` is prime and `False` otherwise. The example usage at the end demonstrates how to use this function with various inputs.