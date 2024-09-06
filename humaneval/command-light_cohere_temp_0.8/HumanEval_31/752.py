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
This function checks whether a given number `n` is prime or not. It uses the particular algorithm that checks divisibility of numbers by squaring up up to the square root of `n` and looking for any divisibility or divisibility of a squared number. The function returns `True` if `n` is prime and `False` otherwise.