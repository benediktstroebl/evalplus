### FibFib Number Sequence Computation
```python
def memoize(func):
    """A simple decorator for memoizing function results."""
    cache = dict()
    def memoized_func(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return memoized_func

@memoize
def fibfib(n: int) -> int:
    """The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    
    Args:
    n: An integer representing the index of the FibFib number to compute.
    
    Returns:
    An integer representing the n-th element of the FibFib number sequence.
    """
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)

# Example usage
if __name__ == "__main__":
    print(fibfib(1))  # Output: 0
    print(fibfib(5))  # Output: 4
    print(fibfib(8))  # Output: 24
```
This script uses a decorator called `memoize` to store the results of expensive function calls and return the cached result when the same inputs occur again. This technique is called memoization.

The `fibfib` function implements the recursive formula for the FibFib sequence. It has been decorated with `memoize` to avoid redundant calculations.

Note that the `fibfib` function has a time complexity of O(n) due to the memoization, whereas the naive recursive implementation would have a time complexity of O(3^n).