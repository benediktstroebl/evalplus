```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.

    A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

    Parameters:
    n (int): The number to be checked for primality

    Returns:
    bool: True if the number is prime, False otherwise

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
    # Check if the number is less than 2, in which case it's not prime
    if n < 2:
        return False
    # Check if the number is 2, which is the only even prime number
    if n == 2:
        return True
    # Check if the number is even, in which case it's not prime
    if n % 2 == 0:
        return False
    # Check odd factors up to the square root of n
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# Test the function
print(is_prime(6))    # False
print(is_prime(101))  # True
print(is_prime(11))   # True
print(is_prime(13441))# True
print(is_prime(61))   # True
print(is_prime(4))    # False
print(is_prime(1))    # False
```

This Python script implements the `is_prime(n)` function, which checks whether a given number `n` is prime or not. It first checks for edge cases (numbers less than 2, the number 2, and even numbers greater than 2), and then checks odd factors up to the square root of `n`. If `n` has no divisors other than 1 and itself, it is a prime number, and the function returns `True`; otherwise, it returns `False`. The function is then tested with the provided examples.