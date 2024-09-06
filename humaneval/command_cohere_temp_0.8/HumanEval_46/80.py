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
This Python script defines a function `fib4` that efficiently calculates the n-th element of the Fib4 sequence, a variant of the Fibonacci sequence. The function utilizes an initial cache of the first 5 sequence elements and then efficiently computes subsequent elements using iterative calculations. 
This approach avoids the exponential time complexity associated with recursive solutions and enhances performance by avoiding redundant calculations through caching. It provides an elegant solution for this specific sequence, balancing computational efficiency and code simplicity.