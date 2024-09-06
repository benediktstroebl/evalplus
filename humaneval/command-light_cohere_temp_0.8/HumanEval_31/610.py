```python
def is_prime(n):
    """Check if a given number is prime."""
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
This code checks if a given number `n` is prime or not. It starts by checking if `n` is less than or equal to 1 and returns `False` since prime numbers are greater than 1. It then checks if `n` is less than or equal to 3 and returns `True` since all primes are divisible by 2 and 3. The function then starts checking for divisibility by testing divisibility with increasing numbers, starting from 5. 

It checks for divisibility by testing only numbers that are less than or equal to the square of the number being tested. This optimization reduces the overall time complexity significantly and can improve the efficiency of the code.