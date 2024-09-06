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
The function `is_prime` determines whether an input number `n` is a prime number, which has exactly one factor. It uses a the a series of conditions and iteration to determine whether the input number is prime.

The function initially determines whether the input number is less than or equal to one and returns `False` if it is. Then, the function determines whether the input number is less than or equal to two and returns `True` if it is. Finally, the function iterates through the square root of the input number, starting from 5, until the square root exceeds the input number. If the input number is divisible by any of these values, the function returns `False`. If the input number is not divisible by any of these values, the function returns `True`.

This function is self-contained and can be used to determine whether a given number is prime or not, which is a fundamental operation in number theory.