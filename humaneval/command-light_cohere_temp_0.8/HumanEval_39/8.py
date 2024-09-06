```python
def prime_fib(n: int):
    if n <= 1:
        return n
    a, b = 2, 3
    for _ in range(n - 2):
        a, b = next((c for c in [a, b] if c == 2))
    return a + b
```