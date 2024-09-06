```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n <= 3:
        return 3
    m, k = 6, 0
    while True:
        if k == (n - 2) // 2:
            break
        m *= int(1 + (k + 1) ** .5)
        k += 1
    return m
```