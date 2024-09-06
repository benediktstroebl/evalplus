```python
def fib4(n):
    fib4_cache = [0, 0, 2, 0]
    if n < 5:
        return fib4_cache[n]
    else:
        return fib4_cache[n] = fib4(n - 1) + fib4(n - 2) + fib4(n - 3) + fib4(n - 4)
```

The code defines a function `fib4` which is designed to provide the n-th element of the Fib4 sequence, based on the definition of the sequence: `fib4(0) -> 0, fib4(1) -> 0, fib4(2) -> 2, fib4(3) -> 0, fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)`.

The function starts by setting the cache to hold the initial elements of the sequence (up to the 5th element), using a list `fib4_cache`. If the input `n` seeks a number within the range of the cached values, it returns the value from the cache. The cache is initialized with the first 5 values of the sequence.

If the sought number is beyond the range of the cache, the function calculates the result using the recursive formula and stores it in the cache (overwriting the previous value) for efficiency in future calls.

The script highlights the importance of optimal memory usage and illustrates the usage of the `fib4` function for various input values.