### Prime Number Checker

Here's a simple Python script that defines a function to check if a given number is prime:
```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.

    Args:
    n (int): The number to check for primality.

    Returns:
    bool: True if n is prime, False otherwise.
    """
    if n <= 1:
        # Numbers less than or equal to 1 are not prime
        return False
    elif n <= 3:
        # 2 and 3 are prime
        return True
    elif n % 2 == 0:
        # Even numbers greater than 2 are not prime
        return False
    elif n % 3 == 0:
        # Numbers that are divisible by 3 are not prime
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            # If n is divisible by any number up to its square root, it's not prime
            return False
        i += 6
    # If n passes all the checks, it's prime
    return True

# Example usage:
print(is_prime(6))  # False
print(is_prime(101))  # True
print(is_prime(11))  # True
print(is_prime(13441))  # True
print(is_prime(61))  # True
print(is_prime(4))  # False
print(is_prime(1))  # False
```
This script uses a simple trial division method to check for primality, which is sufficient for small to medium-sized numbers. For larger numbers, a more efficient algorithm such as the Miller-Rabin primality test or the AKS primality test would be needed.