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
    """The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    This function efficiently computes the n-th element of the fibfib number sequence.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    elif n <= 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)


# Test the function
if __name__ == "__main__":
    print(fibfib(1))    # Expected output: 0
    print(fibfib(5))    # Expected output: 4
    print(fibfib(8))    # Expected output: 24
```

This script employs memoization to optimize the function call for repeated sequence elements, reducing the overall time complexity to O(n).