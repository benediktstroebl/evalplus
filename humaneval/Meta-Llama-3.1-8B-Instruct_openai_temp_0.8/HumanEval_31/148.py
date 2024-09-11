```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.

    Parameters:
    n (int): The number to check for primality.

    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if n <= 1:  # Edge case: numbers less than or equal to 1 are not prime
        return False
    if n <= 3:  # Edge case: 2 and 3 are prime
        return True
    if n % 2 == 0 or n % 3 == 0:  # Edge case: if the number is divisible by 2 or 3, it's not prime
        return False
    i = 5
    while i * i <= n:  # Only need to check up to the square root of n
        if n % i == 0 or n % (i + 2) == 0:  # Check if n is divisible by i or i+2
            return False
        i += 6  # Increment i by 6 to check the next potential divisor
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

This script defines a function `is_prime(n)` that checks whether a given number `n` is prime or not. It uses a simple trial division method to determine primality, which is efficient for small to medium-sized numbers. The function includes several edge cases to handle numbers less than or equal to 1, as well as the special cases of 2 and 3 being prime. The test cases at the end demonstrate the function's correctness.