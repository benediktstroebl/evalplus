```python
def fib4(n: int):
    fib4_cache = [0, 0, 2, 0]
    if n < 0:
        return "Invalid input: n should be a non-negative integer."
    while len(fib4_cache) < n + 1:
        fib4_cache.append(fib4_cache[-1] + fib4_cache[-2] + fib4_cache[-3] + fib4_cache[-4])
    return fib4_cache[n]
```

This script defines a function `fib4` which efficiently calculates the n-th element of the Fib4 sequence, as described in the problem statement. It uses a cache mechanism to store the calculated values and appends new values to the cache iteratively, avoiding recursion as requested. The function returns the appropriate message if n is negative, ensuring the input is a valid non-negative integer.