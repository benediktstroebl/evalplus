```python
def memoize(func):
    """A decorator to memoize the results of expensive function calls."""
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
    The FibFib number sequence is a sequence similar to the Fibbonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).

    Args:
        n (int): The index of the FibFib number to compute.

    Returns:
        int: The n-th element of the FibFib number sequence.
    """
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)


if __name__ == "__main__":
    print(fibfib(1))  # 0
    print(fibfib(5))  # 4
    print(fibfib(8))  # 24
```

This script uses a memoization technique to efficiently compute the n-th element of the FibFib number sequence. The `memoize` decorator caches the results of expensive function calls, so if the function is called again with the same arguments, it returns the cached result instead of recomputing it. This significantly improves the performance of the `fibfib` function for large values of `n`.