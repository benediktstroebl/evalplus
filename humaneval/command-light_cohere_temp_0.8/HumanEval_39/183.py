```python
def prime_fib(n: int):
    if n <= 1:
        return n
    elif n <= 3:
        return 3
    elif n % 2 == 0:
        return 5
    else:
        a = prime_fib(n // 2)
        if a == 2:
            return a + 2
        return a
```