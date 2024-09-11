```python
def memoize(func):
    """A memoization decorator to store computed values."""
    cache = dict()
    def memoized_func(*args):
        if args in cache:
            return cache[args]
        else:
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
    This function efficiently computes the n-th element of the fibfib number sequence.
    
    Args:
        n (int): The index of the element to compute.

    Returns:
        int: The n-th element of the fibfib number sequence.
    """
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)

# Test the function
print(fibfib(1))  # Expected output: 0
print(fibfib(5))  # Expected output: 4
print(fibfib(8))  # Expected output: 24
```

This script first defines a `memoize` decorator that stores computed values to avoid redundant computations. Then it defines the `fibfib` function, which uses the Fibonacci-like recurrence relation to compute the n-th element of the sequence. The function is decorated with `@memoize` to enable memoization. Finally, it tests the function with the provided examples.