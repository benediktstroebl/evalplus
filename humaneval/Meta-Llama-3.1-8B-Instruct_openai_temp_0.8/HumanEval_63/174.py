```markdown
## FibFib Number Sequence

The following Python script efficiently computes the n-th element of the FibFib number sequence.

### Code

```python
def memoize(func):
    """Decorator to store and reuse the results of expensive function calls."""
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
    if n < 0:
        raise ValueError("n must be a non-negative integer")

    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1

    # Use memoization to store and reuse the results
    return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)

### Example Use Cases

print(fibfib(1))  # Output: 0
print(fibfib(5))  # Output: 4
print(fibfib(8))  # Output: 24
```

### Explanation

This script uses memoization to efficiently compute the n-th element of the FibFib number sequence. Memoization is a technique where the results of expensive function calls are stored and reused instead of recomputed. The `memoize` decorator is used to store the results of the `fibfib` function calls.

The `fibfib` function takes an integer `n` as input and returns the n-th element of the FibFib number sequence. The base cases are handled separately, and for `n >= 3`, the function uses the recursive formula `fibfib(n) = fibfib(n-1) + fibfib(n-2) + fibfib(n-3)`.

The memoized function is used to store and reuse the results of the `fibfib` function calls, which significantly improves the performance for large values of `n`.