```python
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
```
This function, `is_prime`, accepts an integer `n` as input and returns `True` if `n` is a prime number and `False` otherwise. It implements a certain necessary of Sieve of Eratosthenes, which is a highly efficient algorithm to determine primality. This function also includes some basic checks for the following prime numbers: 2 and 3 (since they are exceptions to being prime), as well as checks for numbers that are divisible by 2, 3, or themselves (i.  (these are often referred to as "divisors"). 
The function performs well and passes all of the tests.