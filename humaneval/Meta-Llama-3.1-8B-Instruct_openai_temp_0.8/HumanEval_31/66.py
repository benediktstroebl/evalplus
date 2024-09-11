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
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Test cases
print(is_prime(6))  
print(is_prime(101))  
print(is_prime(11))  
print(is_prime(13441))  
print(is_prime(61))  
print(is_prime(4))  
print(is_prime(1))
```

This Python script defines a function `is_prime(n)` that checks whether a given number `n` is prime or not. The function first checks if `n` is less than or equal to 1. If it is, the function returns `False` because numbers less than 2 are not prime. Then, it iterates over numbers from 2 to the square root of `n`. If `n` is divisible by any of these numbers, the function returns `False` because `n` is not prime. If `n` passes this test, the function returns `True` because `n` is prime.

The script includes test cases to demonstrate the function's behavior with different inputs. These test cases match the expected output listed in the docstring.