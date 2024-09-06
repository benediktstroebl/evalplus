```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n % 2 == 0:
        return 6
    else:
        a, b = 3, 5
        for _ in range(n // 2):
            a, b = b, a + b
        if a == b:
            return a
        else:
            return b
```