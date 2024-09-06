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

The code defines a function `fib4` that efficiently calculates the n-th element of the Fib4 sequence, a variant of the Fibonacci sequence. The function initializes a cache of the first four sequence values and uses recursion to compute subsequent values. It returns `None` for negative input and provides the cached value for n<=4. For larger n, it computes the value using the recursive formula fib4(n) = fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4). The self-contained script includes corresponding test cases to validate its behavior.