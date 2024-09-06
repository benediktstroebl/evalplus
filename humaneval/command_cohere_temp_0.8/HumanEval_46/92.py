```python
def fib4(n):
    fib4_cache = [0, 0, 2, 0]
    if n < 0:
        raise ValueError("fib4 is not defined for negative numbers")
    elif n < 5:
        return fib4_cache[n]
    else:
        return fib4_cache[n] = fib4(n - 1) + fib4(n - 2) + fib4(n - 3) + fib4(n - 4)
```

The function `fib4()` uses a cache of the first 5 elements of the sequence to compute the subsequent ones. It uses the cache to avoid redundant computations and returns the n-th element of the Fib4 sequence when provided with a positive integer `n`. It raises a `ValueError` for negative input.