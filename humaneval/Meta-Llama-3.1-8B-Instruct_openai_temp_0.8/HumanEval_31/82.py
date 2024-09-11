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
    if n <= 1:
        # Numbers less than or equal to 1 are not prime
        return False
    elif n <= 3:
        # 2 and 3 are prime
        return True
    elif n % 2 == 0 or n % 3 == 0:
        # If the number is divisible by 2 or 3, it's not prime
        return False
    i = 5
    while i * i <= n:
        # Only need to check up to the square root of n
        if n % i == 0 or n % (i + 2) == 0:
            # If the number is divisible by any number in this range, it's not prime
            return False
        i += 6
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

This script uses a simple algorithm to check if a number is prime. It first checks if the number is less than or equal to 1, in which case it's not prime. Then it checks if the number is 2 or 3, in which case it is prime. Next, it checks if the number is divisible by 2 or 3, in which case it's not prime. Finally, it checks the number for divisibility by all numbers in the range from 5 to the square root of the number, incrementing by 6 each time (since all primes are of the form 6k ± 1). If the number is not divisible by any of these numbers, it's prime.