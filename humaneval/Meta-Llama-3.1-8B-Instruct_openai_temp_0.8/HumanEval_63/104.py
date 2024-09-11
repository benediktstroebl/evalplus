```python
def memoize(func):
    """A decorator to memoize the results of expensive function calls."""
    cache = dict()

    def memoized_func(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return memoized_func


@memoize
def fibfib(n: int) -> int:
    """The FibFib number sequence is a sequence similar to the Fibonacci sequence.
    
    It is defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    
    Args:
        n (int): The index of the FibFib number sequence.
    
    Returns:
        int: The nth element of the FibFib number sequence.
    """
    if n <= 2:
        return 0
    elif n == 3:
        return 1
    else:
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)


if __name__ == "__main__":
    for i in range(1, 9):
        print(f"fibfib({i}) = {fibfib(i)}")
```

This script defines a `fibfib` function that uses memoization to efficiently compute the nth element of the FibFib number sequence. The `memoize` decorator caches the results of previous function calls, so that they can be reused instead of recalculated.

The script then tests the `fibfib` function with various inputs and prints the results.