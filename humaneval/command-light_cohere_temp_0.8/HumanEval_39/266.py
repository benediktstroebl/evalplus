```python
def prime_fib(n: int):
    if n <= 1:
        return n
    elif n == 2:
        return 2
    else:
        a = prime_fib(n // 2)
        b = prime_fib(n % 2)
        return a + b + 2
```