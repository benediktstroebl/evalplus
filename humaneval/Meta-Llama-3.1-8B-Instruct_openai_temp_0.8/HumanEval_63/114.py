```markdown
## FibFib Number Sequence

The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:

- `fibfib(0)` is equal to 0
- `fibfib(1)` is equal to 0
- `fibfib(2)` is equal to 1
- `fibfib(n)` is equal to `fibfib(n-1)` + `fibfib(n-2)` + `fibfib(n-3)`.

### Code

```python
def memoize(func):
    """A simple memoization decorator"""
    cache = dict()

    def memoized_func(*args):
        """Check if the result is cached"""
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    return memoized_func

@memoize
def fibfib(n: int):
    """The n-th element of the FibFib number sequence"""
    if n <= 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibfib(n - 1) + fibfib(n - 2) + fibfib(n - 3)

# Test cases
print(fibfib(1))     # 0
print(fibfib(5))     # 4
print(fibfib(8))     # 24
```

### Explanation

The `fibfib` function is decorated with a simple `memoize` decorator, which caches the results of expensive function calls and returns the cached result when the same inputs occur again.

This approach prevents redundant calculations and significantly improves performance when computing the n-th element of the FibFib sequence for large values of n.

Note that the base cases are handled explicitly to avoid potential stack overflows when using recursion.