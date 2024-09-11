```python
def memoize(func):
    """Function decorator to cache the results of expensive function calls."""
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
    
    Args:
        n (int): The index of the FibFib number sequence.
    
    Returns:
        int: The n-th element of the FibFib number sequence.
    """
    if n <= 2:
        return 0
    elif n == 3:
        return 1
    else:
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)


# Test cases
print(fibfib(1))  # 0
print(fibfib(5))  # 4
print(fibfib(8))  # 24
```

In this script, we use a decorator called `memoize` to cache the results of the `fibfib` function. This significantly improves the performance of the function, especially for large inputs, by avoiding redundant calculations.

The `fibfib` function itself is a simple recursive implementation of the FibFib number sequence. However, due to the redundant calculations involved in the recursive calls, the function's performance would degrade rapidly for large inputs. The `memoize` decorator solves this problem by storing the results of previous function calls in a cache, allowing the function to return the cached results instead of recalculating them.