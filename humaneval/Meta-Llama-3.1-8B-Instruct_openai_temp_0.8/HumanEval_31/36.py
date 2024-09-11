```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.

    A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

    Examples:
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
    if n <= 1:  # Prime numbers are greater than 1
        return False

    for i in range(2, int(n ** 0.5) + 1):  # Check divisors up to the square root of n
        if n % i == 0:  # If n is divisible by i, it's not prime
            return False

    return True  # If no divisors are found, n is prime


# Test cases
print(is_prime(6))   # False
print(is_prime(101)) # True
print(is_prime(11))  # True
print(is_prime(13441)) # True
print(is_prime(61))  # True
print(is_prime(4))   # False
print(is_prime(1))   # False
```

This script uses a simple trial division approach to check if a number is prime. It iterates from 2 to the square root of the number and checks for divisors. If no divisors are found, the number is prime. This approach is efficient for small to medium-sized numbers. For larger numbers, you may want to use more advanced primality tests, such as the Miller-Rabin primality test.