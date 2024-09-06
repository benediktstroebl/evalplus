```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n % 2 == 0:
        return prime_fib(n - 2)
    i = 3
    while i * i <= n:
        if n % i == 0:
            return i
        i += 1
    return i
```