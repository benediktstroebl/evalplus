### Prime Number Checker
#### Python Script

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
    if n <= 1:  # Numbers less than or equal to 1 are not prime
        return False
    if n == 2:  # 2 is the only even prime number
        return True
    if n % 2 == 0:  # All other even numbers are not prime
        return False
    max_divisor = int(n**0.5) + 1  # Only need to check up to the square root of n
    for d in range(3, max_divisor, 2):  # Only need to check odd numbers
        if n % d == 0:
            return False
    return True

# Test cases
print(is_prime(6))    # False
print(is_prime(101))  # True
print(is_prime(11))   # True
print(is_prime(13441))# True
print(is_prime(61))   # True
print(is_prime(4))    # False
print(is_prime(1))    # False
```

This script defines a function `is_prime(n)` that checks whether a given number `n` is prime or not. It uses the following logic:

*   Numbers less than or equal to 1 are not prime.
*   The number 2 is the only even prime number.
*   All other even numbers are not prime.
*   To check if a number is prime, it only needs to check up to the square root of the number (this is because a larger factor of the number would have already been found as a smaller factor).
*   Only need to check odd numbers as potential factors.

The script also includes test cases at the end to verify the correctness of the `is_prime(n)` function.