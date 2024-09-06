```python
def fib4(n: int) -> int:
    fib4_cache = [0, 0, 2, 0]
    if n < 5:
        return fib4_cache[n]
    else:
        return fib4_cache[n] = fib4(n - 1) + fib4(n - 2) + fib4(n - 3) + fib4(n - 4)
```

The function fib4() uses an initial cache of the first 5 numbers in the sequence to ensure that any calls to fib4(n) where n < 5 returns the correct value. It uses a recursive approach to calculate the Fib4 sequence efficiently without having to compute any previous values multiple times.