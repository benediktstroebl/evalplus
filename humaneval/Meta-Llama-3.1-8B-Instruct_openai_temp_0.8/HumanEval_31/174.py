```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.

    A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if n <= 1:  # 1 and numbers less than 1 are not prime
        return False
    if n <= 3:  # 2 and 3 are prime
        return True
    if n % 2 == 0 or n % 3 == 0:  # if the number is divisible by 2 or 3, it's not prime
        return False
    i = 5
    while i * i <= n:  # only need to check up to the square root of n
        if n % i == 0 or n % (i + 2) == 0:  # check for divisors of the form 6k ± 1
            return False
        i += 6
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

This script defines a function `is_prime` that checks whether a given number `n` is prime. It uses a combination of optimizations to improve performance:

1.  It first checks if the number is less than or equal to 1, in which case it's not prime.
2.  It then checks if the number is 2 or 3, in which case it's prime.
3.  It checks if the number is divisible by 2 or 3, in which case it's not prime.
4.  It then checks for divisors of the form 6k ± 1, starting from 5, up to the square root of `n`. If any divisor is found, the function returns `False`.
5.  If no divisors are found, the function returns `True`, indicating that the number is prime.