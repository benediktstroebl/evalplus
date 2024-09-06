```python
def fib4(n):
    fib4_cache = [0, 0, 2, 0]
    if n < 0:
        raise ValueError("fib4 is not defined for negative numbers")
    while len(fib4_cache) <= n:
        fib4_cache.append(fib4_cache[-1] + fib4_cache[-2] + fib4_cache[-3] + fib4_cache[-4])
    return fib4_cache[n]
```

This script defines the `fib4()` function, which efficiently calculates the n-th element of the Fib4 sequence. It utilizes a cache to store calculated values and avoids recursion by using a while loop to populate the cache. The provided tests illustrate the usage and correctness of the function. 

**NOTE**: The initial cache values (`[0, 0, 2, 0]`) are the known base elements of the Fib4 sequence. The cache is then updated in a loop, calculating the next values in the sequence based on the cache's previous values, thereby avoiding the need for recursive calls and their associated overhead.