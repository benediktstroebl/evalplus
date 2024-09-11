### Prime Number Checker
#### Problem Statement
Write a Python function `is_prime(n)` that checks whether a given number `n` is prime or not.

#### Solution
```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.

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
    if n <= 1:  # 1 and numbers less than 2 are not prime
        return False
    if n <= 3:  # 2 and 3 are prime
        return True
    if n % 2 == 0 or n % 3 == 0:  # if n is divisible by 2 or 3, it's not prime
        return False
    i = 5
    while i * i <= n:  # only need to check up to sqrt(n)
        if n % i == 0 or n % (i + 2) == 0:  # check for divisibility by i and i+2
            return False
        i += 6  # increment by 6 to check the next potential prime
    return True
```

#### Explanation
This function uses a simple trial division approach to check for primality. It first handles the edge cases where `n` is less than or equal to 1 (not prime) or 2 or 3 (prime). Then, it checks if `n` is divisible by 2 or 3. If it is, it's not prime. Otherwise, it starts a loop that checks for divisibility by potential prime numbers starting from 5. The loop only needs to check up to the square root of `n`, as any factor larger than that would have a corresponding factor smaller than the square root. The function returns `True` if `n` is prime and `False` otherwise.