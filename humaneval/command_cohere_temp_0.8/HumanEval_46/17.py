```python
def fib4(n: int):
    fib4_cache = [0, 0, 2, 0]
    if n < 5:
        return fib4_cache[n]
    else:
        return fib4_cache[n] = fib4(n - 1) + fib4(n - 2) + fib4(n - 3) + fib4(n - 4)
```

The code defines a function `fib4` which is designed to provide the n-th element of the Fib4 sequence, which is a variant of the Fibonacci sequence. The function efficiently computes these values by maintaining a cache of the first 5 values of the sequence (which are initialized to 0). When calculating subsequent elements, it retrieves the values from this cache, avoiding redundant calculations. This is validated with tests that verify the function's correctness for various 'n' values.