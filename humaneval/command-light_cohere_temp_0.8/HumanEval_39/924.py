```python
def prime_fib(n: int):
    if n <= 1:
        return n
    elif n <= 3:
        return 2
    elif n % 2 == 0:
        return 3
    else:
        i = 5
        while i * i <= n:
            if n % (i + 1) == 0:
                return i
            i += 6
        return next((x for x in range(5) if x * x > n))
```