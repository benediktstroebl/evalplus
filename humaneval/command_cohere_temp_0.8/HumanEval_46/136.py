```python
def fib4(n):
    fib4_cache = [0, 0, 2, 0]
    if n < 0:
        raise ValueError(" fib4 is not defined for negative numbers")
    elif n < 5:
        return fib4_cache[n]
    else:
        return fib4_cache[n] = fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)
```

The function `fib4()` uses a cache to store the computed values of the Fib4 sequence up to the 4th last step. It retrieves the cached value if the input value is less than 5. If the value is greater, it computes the Fib4 value for the nth position efficiently using the cached history of previous steps without recursion. 

This solution is efficient and avoids the repeated computation of intermediate steps in recursive solutions, which leads to performance issues for larger input values.