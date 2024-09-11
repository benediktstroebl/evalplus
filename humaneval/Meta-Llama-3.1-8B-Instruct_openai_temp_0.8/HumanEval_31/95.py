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
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_divisor = int(n**0.5) + 1
    for d in range(3, max_divisor, 2):
        if n % d == 0:
            return False
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

This script defines a function `is_prime(n)` that checks whether a given number `n` is prime or not. The function uses the following conditions to determine if a number is prime:

1. If `n` is less than or equal to 1, it is not prime.
2. If `n` is 2, it is prime.
3. If `n` is even (i.e., `n % 2 == 0`), it is not prime.
4. Otherwise, the function checks if `n` has any divisors other than 1 and itself by iterating from 3 to the square root of `n` in increments of 2. If any divisor is found, the function returns `False`. If no divisors are found, the function returns `True`.

The script includes example usage of the `is_prime(n)` function at the end, which demonstrates its correctness by printing the results of the function for various input values.