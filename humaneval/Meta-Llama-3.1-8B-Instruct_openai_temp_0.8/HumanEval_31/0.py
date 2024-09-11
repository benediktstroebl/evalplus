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
    if n <= 1:  # 1 and numbers less than 1 are not prime
        return False
    if n <= 3:  # 2 and 3 are prime
        return True
    if n % 2 == 0 or n % 3 == 0:  # If the number is divisible by 2 or 3, it's not prime
        return False
    i = 5
    while i * i <= n:  # Only need to check up to the square root of n
        if n % i == 0 or n % (i + 2) == 0:  # Check for divisors of the form 6k ± 1
            return False
        i += 6
    return True


# Test cases
if __name__ == "__main__":
    print(is_prime(6))  # False
    print(is_prime(101))  # True
    print(is_prime(11))  # True
    print(is_prime(13441))  # True
    print(is_prime(61))  # True
    print(is_prime(4))  # False
    print(is_prime(1))  # False
```

This script uses a simple and efficient algorithm to check if a number is prime. It first handles the edge cases where `n` is less than or equal to 1, or `n` is 2 or 3. Then, it checks if `n` is divisible by 2 or 3. Finally, it checks for divisors of the form `6k ± 1` up to the square root of `n`. If `n` is not divisible by any of these, it is prime.