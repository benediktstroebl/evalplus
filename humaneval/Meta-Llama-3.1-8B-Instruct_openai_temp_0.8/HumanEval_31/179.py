```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.

    A prime number is a positive integer greater than 1 that has no positive divisors other than 1 and itself.

    Args:
        n (int): The number to check for primality.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if n <= 1:  # numbers less than or equal to 1 are not prime
        return False
    if n <= 3:  # 2 and 3 are prime
        return True
    if n % 2 == 0 or n % 3 == 0:  # if the number is divisible by 2 or 3, it's not prime
        return False
    i = 5
    while i * i <= n:  # we only need to check up to the square root of n
        if n % i == 0 or n % (i + 2) == 0:  # check divisibility by 6k +/- 1
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

This script defines a function `is_prime(n)` that checks whether a given number `n` is prime. It does this by first checking for the base cases where `n` is less than or equal to 1 (not prime), or `n` is less than or equal to 3 (prime). It then checks for divisibility by 2 and 3, and finally checks for divisibility by 6k +/- 1 using a loop. The function returns `True` if `n` is prime and `False` otherwise. The test cases at the end demonstrate the function's usage.