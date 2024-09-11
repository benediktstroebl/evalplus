```markdown
### FibFib Number Sequence
#### Efficient Computation of the n-th Element

The following Python script calculates the n-th element of the FibFib number sequence, which is a sequence similar to the Fibonacci sequence with a recurrence relation defined as follows:

- fibfib(0) == 0
- fibfib(1) == 0
- fibfib(2) == 1
- fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3)

```python
def memoize(func):
    """Memoize function to store and reuse previous computations."""
    
    cache = dict()

    def memoized_func(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return memoized_func


@memoize
def fibfib(n: int) -> int:
    """The FibFib number sequence is a sequence similar to the Fibbonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    
    Args:
        n (int): The index of the element in the sequence to be computed.
    
    Returns:
        int: The n-th element of the FibFib number sequence.
    """
    if n < 0:
        raise ValueError("Index out of range")
    elif n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)


if __name__ == "__main__":
    # Test cases
    print(fibfib(1))       # Expected output: 0
    print(fibfib(5))       # Expected output: 4
    print(fibfib(8))       # Expected output: 24
```

This implementation uses memoization to store and reuse previous computations, making the function more efficient for larger values of `n`. The `memoize` decorator stores the results of previous function calls in a cache, so that if the function is called with the same arguments again, the cached result is returned instead of recomputing it. This approach avoids redundant calculations and significantly improves performance.