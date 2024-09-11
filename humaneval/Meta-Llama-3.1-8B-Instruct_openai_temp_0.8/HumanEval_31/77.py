```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.

    A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

    Args:
        n (int): The number to check for primality.

    Returns:
        bool: True if n is prime, False otherwise.

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
    if n <= 3:
        # 2 and 3 are prime
        return True
    if n % 2 == 0 or n % 3 == 0:
        # If n is divisible by 2 or 3, it's not prime
        return False
    # Check divisibility up to the square root of n
    for i in range(5, int(n**0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            # If n is divisible by any odd number, it's not prime
            return False
    # If n passes all the checks, it's prime
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

This script defines a function `is_prime` that checks whether a given number `n` is prime or not. It first checks for the special cases where `n` is less than or equal to 1 (not prime), and where `n` is 2 or 3 (prime). Then it checks divisibility by 2 and 3, and finally checks divisibility by all odd numbers up to the square root of `n`. If `n` passes all these checks, it's considered prime. The test cases at the end of the script demonstrate the function's behavior.