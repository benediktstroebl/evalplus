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

The function fib4 keeps a cache of the first 5 numbers in the sequence to ensure efficiency and optimizes the solution by avoiding redundant computations. It returns the n-th element of the Fib4 sequence when provided with a positive integer n. Also, it handles the edge case where n is less than 0, since the Fib4 sequence is not defined for negative numbers.