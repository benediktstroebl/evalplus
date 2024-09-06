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
This Python function checks whether a given number is a prime or not. It performs the simple algorithm that checks divisibility by 2, 3, and divisibility by numbers that are exactly 5 times the square root of the number. The function returns `True` if the number is prime, and `False` otherwise. 

You can use this function to test for primality for any given number.