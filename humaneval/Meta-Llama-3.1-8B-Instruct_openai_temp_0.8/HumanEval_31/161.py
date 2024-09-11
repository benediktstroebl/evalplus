### Prime Number Checker
```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.

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
    if n <= 1:  # 0 and 1 are not prime numbers
        return False
    if n <= 3:  # 2 and 3 are prime numbers
        return True
    if n % 2 == 0 or n % 3 == 0:  # if n is divisible by 2 or 3, it is not prime
        return False
    i = 5
    while i * i <= n:  # only need to check up to the square root of n
        if n % i == 0 or n % (i + 2) == 0:  # check for divisibility by 6k +/- 1
            return False
        i += 6
    return True


if __name__ == "__main__":
    import doctest
    doctest.testmod()
```
This script defines a function `is_prime` that checks whether a given number `n` is prime or not. It uses a simple and efficient algorithm to check for primality. The function returns `True` if `n` is prime and `False` otherwise. The script also includes a test suite that uses the `doctest` module to verify the correctness of the `is_prime` function.