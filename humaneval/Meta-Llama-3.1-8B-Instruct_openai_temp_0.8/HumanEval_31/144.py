```python
def is_prime(n):
    """Return true if a given number is prime, and false otherwise.
    
    A prime number is a positive integer greater than 1 that has no positive divisors other than 1 and itself.
    
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
    if n <= 1:  # Prime numbers are greater than 1
        return False
    if n <= 3:  # 2 and 3 are prime numbers
        return True
    if n % 2 == 0 or n % 3 == 0:  # If the number is divisible by 2 or 3, it's not prime
        return False
    i = 5
    while i * i <= n:  # We only need to check up to the square root of n
        if n % i == 0 or n % (i + 2) == 0:  # Check for divisibility by i and i+2
            return False
        i += 6  # Increment by 6 to check the next two potential divisors
    return True

# Test the function
print(is_prime(6))  # False
print(is_prime(101))  # True
print(is_prime(11))  # True
print(is_prime(13441))  # True
print(is_prime(61))  # True
print(is_prime(4))  # False
print(is_prime(1))  # False
```

This script defines a function `is_prime` that checks whether a given number `n` is prime. The function uses a simple trial division method to check for primality. It starts by checking if the number is less than or equal to 1, in which case it's not prime. If the number is less than or equal to 3, it's prime. Then it checks if the number is divisible by 2 or 3. If it's divisible by either, it's not prime. Finally, it checks for divisibility by all odd numbers up to the square root of `n` using a loop that increments by 6 each time (since we're checking for divisibility by both `i` and `i+2`). If the number is not divisible by any of these, it's prime.