### Prime Number Checker
```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.

    :param n: The number to check for primality.
    :return: True if n is prime, False otherwise.
    """
    if n <= 1:  # 0 and 1 are not prime numbers
        return False
    for i in range(2, int(n ** 0.5) + 1):  # Check divisibility up to the square root of n
        if n % i == 0:  # If n is divisible by any number, it's not prime
            return False
    return True  # If n is not divisible by any number, it's prime

# Test cases
print(is_prime(6))   # False
print(is_prime(101)) # True
print(is_prime(11))  # True
print(is_prime(13441))  # True
print(is_prime(61))   # True
print(is_prime(4))    # False
print(is_prime(1))    # False
```

This script defines a function called `is_prime` that takes an integer `n` as input and returns `True` if `n` is prime and `False` otherwise. The function uses a simple trial division method to check for primality, which is sufficient for small to medium-sized integers. The time complexity of this method is O(√n), making it efficient for most practical purposes.