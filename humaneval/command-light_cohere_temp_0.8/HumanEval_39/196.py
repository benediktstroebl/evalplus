```python
def prime_fib(n: int):
    if n <= 1:
        return n
    elif n <= 3:
        return 3
    else:
        x, y = 5, 2
        for _ in range(n - 4):
            x, y = y, x + y
        return x
```