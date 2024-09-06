```python
def prime_fib(n: int):
    if n <= 1:
        return n
    else:
        return 2 if prime_fib(n - 2) else 3
```