```python
def memoize(func):
    """A decorator to memoize the results of a function."""
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
    """The FibFib number sequence is a sequence similar to the Fibbonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    
    This version uses memoization to efficiently compute the n-th element of the fibfib number sequence.
    """
    if n < 3:
        return 0
    elif n == 3:
        return 1
    else:
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)


# Test the function
if __name__ == "__main__":
    for i in range(1, 9):
        print(f"fibfib({i}) == {fibfib(i)}")
```

This script uses a decorator to memoize the results of the `fibfib` function, allowing it to efficiently compute the n-th element of the fibfib number sequence. It also includes a test section at the end to demonstrate the function's usage.