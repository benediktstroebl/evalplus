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
This Python code defines a function `is_prime` that checks whether a given number `n` is a prime or not. It starts by checking numbers less than or equal to 2, as they are considered prime by default, and then uses a loop with the condition `i * i <= n` to iterate up to the square root of `i`. This loop continues until the square root of the number exceeds the number, and within this loop, it checks for divisibility by `i` and `i + 2`, which are the two largest factors that can divide `n` without leaving a remainder.  This prime divisors.