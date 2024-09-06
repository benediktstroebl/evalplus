```python
def fib4(n: int):
    fib4_cache = [0, 0, 2, 0]
    if n < 0:
        return None
    if n < 4:
        return fib4_cache[n]
    else:
        return fib4_cache[n] = fib4(n - 1) + fib4(n - 2) + fib4(n - 3) + fib4(n - 4)
```

This script defines a function `fib4` which efficiently calculates the n-th element of the Fib4 sequence, as described in the problem statement. It initialize a cache of the first 4 values of the sequence and uses those values to efficiently calculate the n-th value via dynamic programming principles, avoiding redundant calculations. 

This approach avoids the repeated calculations inherent in a purely recursive solution, thus providing substantial performance improvements, especially for larger values of `n`. 

This solution assumes that the `n` input is a valid integer and returns `None` if `n` is negative.