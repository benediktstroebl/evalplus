```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.
    
    A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
    
    Parameters:
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
    if n % 2 == 0 or n % 3 == 0:  # if the number is divisible by 2 or 3, it's not prime
        return False
    i = 5
    while i * i <= n:  # only need to check up to the square root of n
        if n % i == 0 or n % (i + 2) == 0:  # check for divisibility by 6k +/- 1
            return False
        i += 6
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

This script defines a function `is_prime(n)` that checks whether a given number `n` is prime or not. It uses a simple trial division method to check for primality. The function first checks for some special cases (1 and numbers less than 1 are not prime, 2 and 3 are prime) and then checks for divisibility by 2 and 3. If the number is divisible by 2 or 3, it's not prime. Then it checks for divisibility by 6k +/- 1 up to the square root of the number. If the number is not divisible by any of these values, it's prime. The function returns True if the number is prime and False otherwise.