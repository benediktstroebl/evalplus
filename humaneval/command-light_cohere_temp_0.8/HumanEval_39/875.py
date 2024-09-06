```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n % 2 == 0:
        return 1
    if n % 3 == 0:
        return 2
    # Check for other prime factors recursively
    for i in range(5, n + 1, 6):
        if n % i == 0:
            return i
    return n
```