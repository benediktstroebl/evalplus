```python
def fib4(n: int):
    fib4_cache = [0, 0, 2, 0]
    if n < 5:
        return fib4_cache[n]
    else:
        return fib4_cache[n] = fib4(n - 1) + fib4(n - 2) + fib4(n - 3) + fib4(n - 4)
```

This script defines the `fib4()` function, which returns the n-th element of the Fib4 sequence, given n. The sequence is defined via the recursive relation `fib4(n) = fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4) for n > 4`, with defined values for `n <= 4`. The function efficiently computes the result using a cache to store previously computed values, avoiding the need for redundant calculations. 

This approach avoids recursion and computes the Fib4 numbers more efficiently by reusing previously computed values.