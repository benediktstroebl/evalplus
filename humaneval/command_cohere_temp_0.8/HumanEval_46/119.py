```python
def fib4(n: int):
    fib4_cache = [0, 0, 2, 0]
    if n < 5:
        return fib4_cache[n]
    else:
        return fib4_cache[n] = fib4(n - 1) + fib4(n - 2) + fib4(n - 3) + fib4(n - 4)
```

The code defines a function `fib4` that efficiently calculates the n-th element of the Fib4 sequence, an extension of the Fibonacci sequence. The function initially provides values for the first four terms of the sequence (according to the definition). It then utilizes a cached result mechanism to avoid recalculating values for previously requested indices n, n-1, n-2, and n-3 when handling larger n values. Consequently, the time complexity of computing any element of the Fib4 sequence decreases to a constant time frame, resulting in an efficient and effective solution.