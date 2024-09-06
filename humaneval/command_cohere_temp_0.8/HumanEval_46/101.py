```python
def fib4(n: int) -> int:
    fib4_cache = [0, 0, 2, 0]
    if n < 5:
        return fib4_cache[n]
    else:
        return fib4_cache[n] = fib4(n - 1) + fib4(n - 2) + fib4(n - 3) + fib4(n - 4)
```

The function relies on a cached list that stores the values of the first 5 elements of the sequence to ensure efficiency. It returns the n-th element of the Fib4 sequence, as per the definition you provided, for n >= 5, it recursively calculates the value using the definition, and for n < 5, it returns the cached value directly.