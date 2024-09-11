### Prime Number Checker
```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.

    Args:
        n (int): The number to check for primality.

    Returns:
        bool: True if the number is prime, False otherwise.

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
    for i in range(2, int(n ** 0.5) + 1):
        # Check if n has any divisors up to its square root
        if n % i == 0:
            # If n has a divisor, it's not prime
            return False
    # If n has no divisors, it's prime
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
This script defines a function `is_prime` that checks whether a given number `n` is prime or not. It returns `True` if `n` is prime and `False` otherwise. The function uses a simple trial division method to check for primality. It only checks divisors up to the square root of `n`, which is a sufficient condition for checking primality. The example usage at the end demonstrates the function's behavior with several test cases.