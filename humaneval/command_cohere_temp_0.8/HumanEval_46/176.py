```python
def fib4(n: int):
    fib4_cache = [0, 0, 2, 0]
    if n < 0:
        return "Invalid input: n should be a non-negative integer."
    while len(fib4_cache) < n + 1:
        fib4_cache.append(fib4_cache[-1] + fib4_cache[-2] + fib4_cache[-3] + fib4_cache[-4])
    return fib4_cache[n]
```

This script defines the `fib4` function, which returns the n-th element of the Fib4 sequence, given as input n. It initializes a cache mechanism to store computed values and iteratively computes the Fib4 values up to `n` using a loop, avoiding recursion as stipulated. The script includes a basic input validation to ensure that `n` is a non-negative integer.