```python
def prime_fib(n: int):
    if n <= 1:
        return n
    elif n <= 3:
        return 3
    elif n % 2 == 0:
        return 5
    else:
        i = 5
        while i * i <= n:
            if n % (i + 1) == 0:
                return i
            i += 6
        return next(i for i in range(5) if n % i == 0) + 2
```