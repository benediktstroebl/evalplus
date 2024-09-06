```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n <= 3:
        return 3
    if n % 2 == 0:
        return 5
    a, b = 6, 7
    for _ in range(n - 5):
        a, b = b, a + b
    return a
```