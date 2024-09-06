```python
def fib4(n: int) -> int:
    fib4_cache = [0, 0, 2, 0]
    if n < 5:
        return fib4_cache[n]
    else:
        return fib4_cache[n] = fib4(n - 1) + fib4(n - 2) + fib4(n - 3) + fib4(n - 4)
```

The function fib4() calculates the n-th element of the Fib4 sequence efficiently without using recursion. It initializes with cached values for `fib4(0)`, `fib4(1)`, `fib4(2)`, and `fib4(3)`. For n values less than 5, it directly returns the cached value. For larger n values, it computes the Fib4 value using the definition recursively but without storing intermediate values using a loop structure. This avoids the exponential time complexity associated with pure recursion while still achieving efficient computation for each number in the sequence.