```python
def prime_fib(n: int):
    if n <= 1:
        return n
    elif n == 2:
        return 2
    else:
        a, b = 3, 5
        for _ in range(2, n):
            a, b = b, a + b + 1
        return b
```