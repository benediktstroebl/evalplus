```python
def fibfib(n):
    # Initialize the cache with first few terms
    cache = [0, 0, 1]
    for i in range(3, n+1):
        cache.append(cache[i-1] + cache[i-2] + cache[i-3])
    return cache[n]
```

This approach uses a cache to store previously computed values, eliminating the need to recompute them. It initializes the cache with the first few terms of the sequence, and then iteratively adds values to the cache. The final result is the last value in the cache, which represents the n-th FibFib number.

To use this function, you can call it with a given value of n, which represents the position in the FibFib sequence you want to compute:
```python
>>> fibfib(1)
0
>>> fibfib(5)
4
>>> fibfib(8)
24
```

The script efficiently computes the n-th element of the FibFib sequence in O(n) time complexity, demonstrating an optimized approach that builds upon previous terms without redundant computations.