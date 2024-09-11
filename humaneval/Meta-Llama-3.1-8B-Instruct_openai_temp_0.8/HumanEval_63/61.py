```markdown
**FibFib Number Sequence Calculation**
======================================

This Python script computes the n-th element of the FibFib number sequence efficiently.

### Code

```python
def memoize(func):
    """A decorator to memoize the results of expensive function calls."""
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

    Args:
        n (int): The index of the FibFib number sequence.

    Returns:
        int: The n-th element of the FibFib number sequence.
    """
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)


# Example usage:
if __name__ == "__main__":
    print(fibfib(1))  # Output: 0
    print(fibfib(5))  # Output: 4
    print(fibfib(8))  # Output: 24
```

### Explanation

This script uses a decorator `memoize` to store the results of expensive function calls in a cache. The `fibfib` function is decorated with `memoize` to take advantage of this optimization.

The `fibfib` function recursively calculates the n-th element of the FibFib number sequence. To avoid redundant computations, the function uses the decorator to store the results of previously computed values in a cache. This optimization significantly improves the performance of the function for large values of `n`.

### Usage

You can run the script to test the `fibfib` function with different inputs. The example usage at the end of the script demonstrates how to use the function to compute the n-th element of the FibFib number sequence.