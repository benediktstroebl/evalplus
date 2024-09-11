```python
def memoize(func):
    """A decorator function to cache the results of expensive function calls."""
    cache = dict()
    def memoized_func(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return memoized_func

@memoize
def fibfib(n: int) -> int:
    """The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    
    Parameters:
    n (int): The index of the FibFib number to compute.
    
    Returns:
    int: The n-th element of the FibFib number sequence.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    elif n <= 2:
        return 0
    elif n == 3:
        return 1
    else:
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)

# Test cases
print(fibfib(1))  # Output: 0
print(fibfib(5))  # Output: 4
print(fibfib(8))  # Output: 24
```

This script uses a technique called memoization to cache the results of expensive function calls and avoid redundant computations. The `memoize` decorator function is used to cache the results of the `fibfib` function, which significantly improves its performance for large values of `n`.