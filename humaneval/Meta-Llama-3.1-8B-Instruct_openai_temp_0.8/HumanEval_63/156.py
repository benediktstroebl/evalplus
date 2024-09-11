```python
def memoize(func):
    """A simple memoization decorator to cache the results of expensive function calls."""
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

    Args:
        n (int): The index of the FibFib number to compute.

    Returns:
        int: The n-th element of the FibFib number sequence.
    """
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)

# Example usage:
print(fibfib(1))  # Output: 0
print(fibfib(5))  # Output: 4
print(fibfib(8))  # Output: 24
```

In this solution, we use a memoization decorator to cache the results of the `fibfib` function. This is necessary because the function has overlapping subproblems and could otherwise suffer from exponential time complexity. The decorator stores the results of previously computed values in a dictionary, which allows the function to return the cached results instead of recomputing them.

The `fibfib` function itself is relatively simple. It handles the base cases (n = 0, 1, and 2) and otherwise recursively calls itself with the indices n-1, n-2, and n-3 to compute the result. Because the results are cached, the function can efficiently compute arbitrary values of the FibFib sequence.