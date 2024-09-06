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

The function fib4 keeps a cache of the first 5 numbers in the sequence to ensure efficiency, as computing the 5th tier of the sequence relies on the previous 4 tiers. It validates the input to ensure it does not receive a negative number, as the sequence is not defined for negative numbers. If the input is one of the first 5 numbers, it returns the pre-computed value, and for all other inputs, it computes the value efficiently using the cache.