```python
def fib4(n: int):
    fib4_cache = [0, 0, 2, 0]
    if n < 0:
        return "Invalid input: n should be a non-negative integer."
    while len(fib4_cache) <= n:
        fib4_cache.append(fib4_cache[-1] + fib4_cache[-2] + fib4_cache[-3] + fib4_cache[-4])
    return fib4_cache[n]
```

This script defines a function `fib4` which efficiently calculates the n-th element of the Fib4 sequence, as described in the problem statement. It utilizes a cache mechanism to avoid redundant calculations and computes the Fib4 value for a given n. The initial cache values [0, 0, 2, 0] are the first few elements of the Fib4 sequence. The function then appends the next Fib4 value in the cache by summing the previous four elements, iterating until the cache length exceeds n. Finally, it returns the n-th Fib4 value from the cache. 

This solution efficiently calculates the Fib4 values without recursion and delivers the correct results for the provided test cases.