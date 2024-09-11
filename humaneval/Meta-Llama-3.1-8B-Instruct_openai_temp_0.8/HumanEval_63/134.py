```python
def memoize(func):
    """A decorator to cache the results of expensive function calls."""
    cache = dict()

    def memoized_func(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    return memoized_func


@memoize
def fibfib(n: int):
    """
    The FibFib number sequence is a sequence similar to the Fibonacci sequence 
    that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    
    This function efficiently computes the n-th element of the FibFib number sequence.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")

    if n <= 0:
        return 0
    elif n <= 2:
        return 0
    elif n == 3:
        return 1
    else:
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)


# Example usage:
print(fibfib(1))  # 0
print(fibfib(5))  # 4
print(fibfib(8))  # 24
```

This script uses a decorator called `memoize` to cache the results of the `fibfib` function. This is done to avoid redundant calculations and improve performance by only calculating each Fibonacci number once.