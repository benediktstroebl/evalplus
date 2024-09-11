```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.

    A prime number is a positive integer that is divisible only by itself and 1.

    Args:
        n (int): The number to check for primality.

    Returns:
        bool: True if n is prime, False otherwise.

    Example:
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
    i = 5
    while i * i <= n:
        # Check divisibility up to the square root of n
        if n % i == 0 or n % (i + 2) == 0:
            # If n is divisible by any odd number, it's not prime
            return False
        i += 6
    return True


# Example usage:
print(is_prime(6))   # False
print(is_prime(101)) # True
print(is_prime(11))  # True
print(is_prime(13441))#True
print(is_prime(61))  # True
print(is_prime(4))   # False
print(is_prime(1))   # False
```

This Python script defines a function `is_prime(n)` to check whether a given number `n` is prime or not, based on the following rules:

1. A number less than or equal to 1 is not prime.
2. 2 and 3 are prime numbers.
3. A number is not prime if it is divisible by 2 or 3.
4. For a number greater than 3, check divisibility up to its square root by incrementing the divisor by 6 (since all primes are of the form 6k ± 1, for k >= 1).

The script provides example usage to demonstrate the function's correctness.