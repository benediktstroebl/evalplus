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
This Python function, `is_prime`, takes an integer `n` as input and returns `True` if `n` is a prime number, and `False` otherwise. 

The function uses a combination of basic primality checks, including divisibility by 2 and 3, and the fundamental theorem of arithmetic. 

The function then iterates through increasing prime numbers (starting from 5) until it reaches or is less than the given number `n`.  This process helps identify any divisibility by prime numbers.