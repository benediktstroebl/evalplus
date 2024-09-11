### Prime Number Checker
#### Solution using a naive approach

```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.

    Args:
        n (int): The number to check for primality.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if n <= 1:  # 1 and numbers less than 1 are not prime
        return False
    if n <= 3:  # 2 and 3 are prime
        return True
    if n % 2 == 0 or n % 3 == 0:  # Numbers divisible by 2 or 3 are not prime
        return False
    i = 5
    while i * i <= n:  # Only need to check up to the square root of n
        if n % i == 0 or n % (i + 2) == 0:  # Check divisibility by i and i + 2
            return False
        i += 6  # Increment i by 6 to check the next pair of potential divisors
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

This script uses a naive approach to check for primality by trial division. It checks divisibility of the input number `n` by incrementing `i` by 6 (to check the next pair of potential divisors) and stops when `i * i` exceeds `n`. This approach has a time complexity of O(sqrt(n)).