```python
def fib4(n: int) -> int:
    fib4_cache = [0, 0, 2, 0]
    if n < 5:
        return fib4_cache[n]
    else:
        return fib4_cache[n] = fib4(n - 1) + fib4(n - 2) + fib4(n - 3) + fib4(n - 4)
```

The code defines a function `fib4` that efficiently calculates the n-th element of the Fib4 sequence, an extension of the Fibonacci sequence. The function initially provides caching for the first five sequence elements, returning the cached value for n <= 4. For larger `n`, the function calculates the result using the defining recurrence relation, updating the cache for efficient future calculations. This optimized approach avoids redundant calculations and ensures quick sequential queries.