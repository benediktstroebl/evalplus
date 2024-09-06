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
This function, `is_prime`, takes an integer `n` as input and returns `True` if `n` is a prime number, and `False` otherwise. It uses some of the value thresholds, checks divisibility by 2 and 3, and then uses the `i` loop to check divisibility up to the square root of `i`. 

This is the simplest implementation of the `is_prime` function, which follows the standard definition of a prime number.