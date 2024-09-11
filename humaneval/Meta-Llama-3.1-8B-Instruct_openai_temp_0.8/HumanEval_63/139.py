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
def fibfib(n: int):
    """The FibFib number sequence is a sequence similar to the Fibbonacci sequnece 
    that's defined as follows:
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


# Test cases
print(fibfib(1))  # 0
print(fibfib(5))  # 4
print(fibfib(8))  # 24
```

This script uses a decorator called `memoize` to store the results of expensive function calls and reuse them when the function is called again with the same arguments. This technique is called memoization.

The `fibfib` function uses the memoized decorator to optimize its performance. If `n` is less than or equal to 1, the function returns 0. If `n` is 2, the function returns 1. For `n` greater than 2, the function calls itself recursively three times with decreasing values of `n`, and sums the results. The `memoize` decorator ensures that these recursive calls are only made once for each value of `n`, avoiding redundant calculations.