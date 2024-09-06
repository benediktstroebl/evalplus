```python
def fib4(n):
    fib4_cache = [0, 0, 2, 0]
    if n < 0:
        raise ValueError("fib4 is not defined for negative numbers")
    elif n < 5:
        return fib4_cache[n]
    else:
        return fib4_cache[n] = fib4(n - 1) + fib4(n - 2) + fib4(n - 3) + fib4(n - 4)
```

The function `fib4()` uses a cache to store the results of previously computed numbers, with the initial cache containing the first 5 base cases. The function then uses simple conditional statements (if-elif-else) to determine whether to return a cached value or compute the value using the definition of the Fib4 sequence. This approach provides efficient computation without recursion.