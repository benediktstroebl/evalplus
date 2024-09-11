### Prime Number Checker
#### A Python Function to Determine if a Given Number is Prime
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
    if n <= 1:
        # Numbers less than or equal to 1 are not prime
        return False
    if n == 2:
        # 2 is the only even prime number
        return True
    if n % 2 == 0:
        # All other even numbers are not prime
        return False
    # Check odd factors up to the square root of n
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            # If n is divisible by any odd factor, it is not prime
            return False
    # If no factors are found, n is prime
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
This script defines the `is_prime` function, which takes an integer `n` as input and returns `True` if it is prime, and `False` otherwise. The function first checks for the base cases where `n` is less than or equal to 1 (not prime) or `n` is 2 (prime). It then checks for even factors, as all other even numbers are not prime. Finally, it checks odd factors up to the square root of `n` using a for loop, and returns `False` if any factor is found. If no factors are found, the function returns `True`, indicating that `n` is prime.