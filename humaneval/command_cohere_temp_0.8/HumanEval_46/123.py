```python
def fib4(n):
    fib4_cache = [0, 0, 2, 0]
    if n < 5:
        return fib4_cache[n]
    else:
        return fib4_cache[n] = fib4(n - 1) + fib4(n - 2) + fib4(n - 3) + fib4(n - 4)
```

The code defines a function `fib4` which is designed to provide the n-th element of the Fib4 sequence, based on the definition of the sequence: `fib4(0) -> 0, fib4(1) -> 0, fib4(2) -> 2, fib4(3) -> 0, fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)`

The function relies on a cache mechanism to store the results of the first 5 elements (which are all 0 at the beginning). When `n` is less than 5, the function directly returns the cached value. This helps ensure the function is efficient by avoiding unnecessary calculations. The cache is a list named `fib4_cache`. 

When `n` is greater than or equal to 5, the function calculates the `n`-th element by recursively summing the previous four elements in the sequence, using the cached values, and stores the result back into the `fib4_cache` for future use. 

This approach strikes a balance between optimization and brevity, providing an efficient solution to the problem without requiring an inordinate amount of code.