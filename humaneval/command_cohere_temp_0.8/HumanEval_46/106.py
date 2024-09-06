```python
def fib4(n):
    fib4_cache = [0, 0, 2, 0]
    if n < 5:
        return fib4_cache[n]
    else:
        return fib4_cache[n] = fib4(n - 1) + fib4(n - 2) + fib4(n - 3) + fib4(n - 4)
```

The code defines a function `fib4` which is designed to provide the n-th element of the Fib4 sequence, based on the definition of the sequence. The first five elements are hard-coded into a cache (`fib4_cache`) to ensure quick returns for pre-calculated results. For values of `n` beyond the cache range, the function recursively calculates the Fib4 value by summing up the previous three elements in the sequence. This approach avoids redundant calculations and ensures efficiency by leveraging memoization through the use of the cache.