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
The function `is_prime` checks whether a given number `n` is prime or not. It first handles simple special cases of small numbers, then, it checks divisibility by all divisors up to the square root of `n`, using a while loop. 

Finally, it returns `True` if `n` is a prime number, and `False` otherwise.