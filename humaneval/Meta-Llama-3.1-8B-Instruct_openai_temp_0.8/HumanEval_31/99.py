Here is a Python script that defines the `is_prime` function:
```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.

    A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

    Args:
        n (int): The number to check for primality.

    Returns:
        bool: True if n is prime, False otherwise.

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
        return False  # numbers less than or equal to 1 are not prime
    if n == 2:
        return True  # 2 is the only even prime number
    if n % 2 == 0:
        return False  # all other even numbers are not prime
    # check odd divisors up to the square root of n
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# test cases
print(is_prime(6))  # False
print(is_prime(101))  # True
print(is_prime(11))  # True
print(is_prime(13441))  # True
print(is_prime(61))  # True
print(is_prime(4))  # False
print(is_prime(1))  # False
```
This implementation takes advantage of the fact that a larger factor of n must be a multiple of a smaller factor that has already been checked. It only checks odd divisors up to the square root of n, which significantly improves performance for large inputs.