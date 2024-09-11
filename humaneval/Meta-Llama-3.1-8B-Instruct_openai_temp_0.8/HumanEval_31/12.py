```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.

    A prime number is a number greater than 1 that has no positive divisors other than 1 and itself.

    Args:
        n (int): The number to check for primality.

    Returns:
        bool: True if the number is prime, False otherwise.

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
    if n <= 1:
        # Numbers less than or equal to 1 are not prime
        return False
    if n == 2:
        # 2 is the only even prime number
        return True
    if n % 2 == 0:
        # All other even numbers are not prime
        return False
    # Check odd factors up to the square root of n
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            # If n is divisible by any of these factors, it's not prime
            return False
    # If n is not divisible by any of these factors, it's prime
    return True

# Test the function
print(is_prime(6))  # False
print(is_prime(101))  # True
print(is_prime(11))  # True
print(is_prime(13441))  # True
print(is_prime(61))  # True
print(is_prime(4))  # False
print(is_prime(1))  # False
```
This Python script defines a function `is_prime(n)` that checks whether a given number `n` is prime or not. It uses a simple trial division method to check for factors up to the square root of `n`, which is an efficient way to do this. The function returns `True` if `n` is prime and `False` otherwise. The script also includes example use cases and test cases to demonstrate how the function works.