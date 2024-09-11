```python
def memoize(func):
    """A decorator to memoize function results."""
    cache = dict()

    def memoized_func(*args):
        """Return the memoized function result."""
        if args in cache:
            return cache[args]
        else:
            result = func(*args)
            cache[args] = result
            return result

    return memoized_func


@memoize
def fibfib(n: int):
    """The FibFib number sequence is a sequence similar to the Fibbonacci sequence.
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    
    :param n: The position of the number in the sequence.
    :return: The number at position n in the sequence.
    """
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)


if __name__ == "__main__":
    # Test cases
    print(fibfib(1))  # Output: 0
    print(fibfib(5))  # Output: 4
    print(fibfib(8))  # Output: 24
```

This script uses memoization to store the results of expensive function calls so that they can be reused instead of recalculated. This makes the function much more efficient for larger inputs. The `memoize` decorator is a reusable function that can be applied to any function to add memoization.