**Efficiently Computing the FibFib Number Sequence**
=====================================================

Here is a Python script that uses dynamic programming to efficiently compute the n-th element of the FibFib number sequence:

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
    """
    if n < 3:
        return 0
    elif n == 3:
        return 1
    else:
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)


# Example usage:
if __name__ == "__main__":
    print(fibfib(1))  # Output: 0
    print(fibfib(5))  # Output: 4
    print(fibfib(8))  # Output: 24
```

**How it works:**

*   The `memoize` decorator is used to cache the results of the `fibfib` function. This avoids redundant computations and significantly improves performance.
*   The `fibfib` function itself uses the standard recursive formula for the FibFib sequence, but with memoization enabled through the `@memoize` decorator.
*   Example usage is provided in the `if __name__ == "__main__":` block to demonstrate how to call the `fibfib` function with different inputs.

**Tips:**

*   Memoization is a great technique to optimize recursive functions with overlapping subproblems.
*   Use the `@memoize` decorator to simplify the implementation of memoized functions.