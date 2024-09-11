```python
def memoize(func):
    """A decorator function that caches the results of expensive function calls and returns the cached result when the same inputs occur again."""
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
    The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).

    Args:
    n (int): The position of the element in the FibFib sequence.

    Returns:
    int: The nth element of the FibFib sequence.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")

    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1

    # Recursive case
    return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)


# Test cases
if __name__ == "__main__":
    print(fibfib(1))  # Output: 0
    print(fibfib(5))  # Output: 4
    print(fibfib(8))  # Output: 24
```

This script defines a `memoize` decorator that caches the results of expensive function calls. The `fibfib` function is then decorated with this memoizer. This approach solves the problem efficiently by avoiding redundant computations and reducing the time complexity to O(n), where n is the input number.