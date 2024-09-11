```python
def is_prime(n):
    """
    Return True if a given number is prime, and False otherwise.

    A prime number is a positive integer greater than 1 that has no positive divisors other than 1 and itself.
    """
    if n <= 1:  # numbers less than or equal to 1 are not prime
        return False
    for i in range(2, int(n ** 0.5) + 1):  # check divisors up to the square root of n
        if n % i == 0:  # if n is divisible by i, it's not prime
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

This script defines a function `is_prime(n)` that checks whether a given number `n` is prime. It returns `True` if `n` is prime and `False` otherwise. The function uses a simple trial division method to check for primality, which is sufficient for small to moderate-sized integers. For larger integers, more advanced algorithms like the Miller-Rabin primality test may be necessary.

The test cases at the end of the script verify that the `is_prime(n)` function works correctly for the specified inputs.