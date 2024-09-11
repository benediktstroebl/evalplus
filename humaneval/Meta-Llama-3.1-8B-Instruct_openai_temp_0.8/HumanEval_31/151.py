```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.

    A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

    Args:
        n (int): The number to check for primality.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if n <= 1:  # 1 and numbers less than 1 are not prime
        return False
    for i in range(2, int(n**0.5) + 1):  # check up to the square root of n
        if n % i == 0:  # if n is divisible by any number, it's not prime
            return False
    return True

# Test the function
print(is_prime(6))   # False
print(is_prime(101)) # True
print(is_prime(11))  # True
print(is_prime(13441))# True
print(is_prime(61))  # True
print(is_prime(4))   # False
print(is_prime(1))   # False
```

This script defines a function `is_prime(n)` that checks whether a given number `n` is prime or not. It then tests this function with the provided test cases. The function works by checking all numbers from 2 up to the square root of `n` to see if `n` is divisible by any of them. If it finds a divisor, it returns False; otherwise, it returns True. The square root of `n` is used as an upper bound because a larger factor of `n` would be a multiple of smaller factor that has already been checked.