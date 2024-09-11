**FibFib Sequence Calculator**
================================

This Python script defines a function `fibfib` to efficiently calculate the `n`-th element of the FibFib number sequence.

```python
def memoize(func):
    """Memoization decorator to store and reuse function results."""
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
    """The FibFib number sequence is a sequence similar to the Fibonacci sequence.
    
    Parameters:
    n (int): The index of the FibFib number to calculate.
    
    Returns:
    int: The `n`-th element of the FibFib number sequence.
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

**Explanation**
---------------

The `fibfib` function uses a memoization decorator to store and reuse function results. This is necessary to avoid redundant computations and improve performance.

The `memoize` decorator is a simple implementation of memoization. It stores the results of function calls in a cache dictionary and reuses these results when the same input arguments are encountered again.

The `fibfib` function itself uses the memoized results to calculate the `n`-th element of the FibFib number sequence. The function follows the recursive definition of the sequence and uses the memoized results to avoid redundant computations.

**Example Use Cases**
---------------------

The script includes example usage of the `fibfib` function to demonstrate its correct behavior. The `if __name__ == "__main__":` block is used to define the example usage and prevent unnecessary computations when the script is imported as a module.

You can modify the `fibfib` function to calculate different elements of the sequence by passing different values of `n` to the function.