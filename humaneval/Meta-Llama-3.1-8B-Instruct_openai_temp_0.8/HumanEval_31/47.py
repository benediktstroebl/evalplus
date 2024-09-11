### Prime Number Checker
```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.

    A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

    >>> is_prime(6)
    False
    >>> is_prime(101)
    True
    >>> is_prime(11)
    True
    >>> is_prime(13441)
    True
    >>> is_prime(61)
    True
    >>> is_prime(4)
    False
    >>> is_prime(1)
    False
    """
    if n <= 1:
        # Prime numbers are greater than 1
        return False
    for i in range(2, int(n**0.5) + 1):
        # Check divisibility up to the square root of n
        if n % i == 0:
            # If n is divisible by any number, it's not prime
            return False
    # If n is not divisible by any number, it's prime
    return True

# Test cases
print(is_prime(6))    # False
print(is_prime(101))  # True
print(is_prime(11))   # True
print(is_prime(13441))# True
print(is_prime(61))   # True
print(is_prime(4))    # False
print(is_prime(1))    # False
```
This script defines a function `is_prime(n)` that checks whether a given number `n` is prime or not. It uses a simple trial division method to check for prime numbers. The function returns `True` if the number is prime and `False` otherwise. The provided test cases are also included in the script to demonstrate its usage.