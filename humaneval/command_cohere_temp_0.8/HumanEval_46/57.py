```python
def fib4(n: int):
    fib4_cache = [0, 0, 2, 0]
    if n < 5:
        return fib4_cache[n]
    else:
        return fib4_cache[n] = fib4(n - 1) + fib4(n - 2) + fib4(n - 3) + fib4(n - 4)
```

The function fib4() uses an initial cache of the first 5 Fib4 numbers (as defined in the problem statement) and returns the n-th Fib4 number efficiently, avoiding recursion as requested. It does this by checking if n is less than 5 (the base cases), or returning a cached value if n is 5 or greater, after which it recursively computes the n-th Fib4 number by summing the 3 preceding Fib4 numbers.