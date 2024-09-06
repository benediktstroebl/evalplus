```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n % 2 == 0:
        return 3
    if n % 3 == 0:
        return 5
    i = 5
    while i * i <= n:
        if n % i == 0:
            return i
        i += 6
    return n
```