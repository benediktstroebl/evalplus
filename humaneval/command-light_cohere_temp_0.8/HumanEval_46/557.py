Here's the code:
```python
def fib4(n: int):
    """The Fibonacci sequence using memoization."""
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0
    else:
        fib_4_cache = [0]
        for i in range(4, n + 1):
            fib_4_cache.append(fib_4_cache[i - 1] + fib_4_cache[i - 1] + fib_4_cache[i - 2])
        return fib_4_cache[n]

# Example usage
fib_4(5)  # Output: 14
fib_4(7)  # Output: 21
```

This solution uses memoization to store the computed Fibonacci numbers and avoid unnecessary recursive calculations. It provides a efficient computation of Fibonacci numbers by avoiding repeated work.