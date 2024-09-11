```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.
    
    A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
    
    Parameters:
    n (int): The number to check for primality.
    
    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if n <= 1:  # 1 and numbers less than 1 are not prime
        return False
    if n <= 3:  # 2 and 3 are prime
        return True
    if n % 2 == 0 or n % 3 == 0:  # numbers divisible by 2 or 3 are not prime
        return False
    i = 5
    while i * i <= n:  # only need to check up to the square root of n
        if n % i == 0 or n % (i + 2) == 0:  # check divisibility by i and i + 2
            return False
        i += 6  # increment by 6 to check the next possible factor
    return True

# Test cases
print(is_prime(6))   # False
print(is_prime(101)) # True
print(is_prime(11))  # True
print(is_prime(13441)) # True
print(is_prime(61))  # True
print(is_prime(4))   # False
print(is_prime(1))   # False
```

This script defines a function `is_prime(n)` that checks whether a given number `n` is prime or not. It uses a combination of conditions to quickly eliminate non-prime numbers and then checks for divisibility by possible factors up to the square root of `n`. The test cases at the end demonstrate the function's correctness.