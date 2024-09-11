### Prime Number Checker

```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.

    Args:
        n (int): The number to check for primality.

    Returns:
        bool: True if n is prime, False otherwise.
    """
    if n <= 1:  # Numbers less than or equal to 1 are not prime
        return False

    if n == 2:  # 2 is the only even prime number
        return True

    if n % 2 == 0:  # All other even numbers are not prime
        return False

    # Check odd factors up to the square root of n
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False

    # If no factors are found, n is prime
    return True


# Example use cases
print(is_prime(6))  # False
print(is_prime(101))  # True
print(is_prime(11))  # True
print(is_prime(13441))  # True
print(is_prime(61))  # True
print(is_prime(4))  # False
print(is_prime(1))  # False
```

This script uses a simple algorithm to check for primality:

*   If the number is less than or equal to 1, it is not prime.
*   If the number is 2, it is prime.
*   If the number is even (not 2), it is not prime.
*   Otherwise, check odd factors up to the square root of the number. If any factors are found, the number is not prime. If no factors are found, the number is prime.