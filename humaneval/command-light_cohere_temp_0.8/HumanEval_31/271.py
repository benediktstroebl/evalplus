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
This function, `is_prime`, determines whether a given number is a prime or not. It accepts an integer `n` as input and outputs a boolean value indicating whether `n` is prime or not. 

The function employs trial and error, checking for divisibility up to the square root of the number and returning `True` if the number passes all tests and `False` otherwise.