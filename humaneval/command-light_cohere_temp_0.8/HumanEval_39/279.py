```python
def prime_fib(n: int):
    if n <= 1:
        return n
    elif n <= 3:
        return 2
    else:
        a, b = 5, 2
        for _ in range(n - 4):
            a, b = (a + b) % 1, b
        return a
```