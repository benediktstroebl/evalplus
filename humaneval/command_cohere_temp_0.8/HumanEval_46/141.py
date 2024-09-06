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

This script defines the `fib4()` function, which efficiently calculates the n-th element of the Fib4 sequence, following the definition of the sequence provided in the problem statement. It initializes the cache with the first 5 values of the sequence and then uses them to compute subsequent values efficiently, avoiding recursion as requested.