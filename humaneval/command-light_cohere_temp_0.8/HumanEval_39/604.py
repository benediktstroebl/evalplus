```python
def prime_fib(n: int):
    if n <= 1:
        return n
    else:
        a, b = 2, 3
        for _ in range(n - 2):
            a, b = next((a + b) % 2, a + b + 1)
        return b
```