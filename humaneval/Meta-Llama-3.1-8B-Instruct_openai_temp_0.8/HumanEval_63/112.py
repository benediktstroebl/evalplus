```python
def memoize(func):
    """A decorator to memoize the results of a function.
    
    Args:
        func: The function to memoize.
    
    Returns:
        A memoized version of the function.
    """
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
    """The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    
    Args:
        n: The index of the element in the FibFib sequence.
    
    Returns:
        The n-th element of the FibFib sequence.
    """
    if n < 2:
        return 0
    elif n == 2:
        return 1
    else:
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)


# Test the function
print(fibfib(1))  # Output: 0
print(fibfib(5))  # Output: 4
print(fibfib(8))  # Output: 24
```

In this code, we use a memoization decorator to cache the results of the `fibfib` function. This is necessary because the function is recursive and uses a lot of repeated computations, which can be very inefficient. The memoization decorator stores the results of the function in a cache, so that if the function is called again with the same arguments, it can just return the cached result instead of recalculating it.

The `fibfib` function itself is relatively simple. It uses the standard recursive formula for the FibFib sequence, but adds a check for the base cases (n < 2) to avoid unnecessary computations.