```python
def fibfib(n: int):
    """The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    Please write a function to efficiently compute the n-th element of the FibFib number sequence.
    >>> fibfib(1)
    0
    >>> fibfib(5)
    4
    >>> fibfib(8)
    24
    """
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)
```

This script defines the `fibfib` function, which is called with a positive integer `n` and returns the `n`-th element of the FibFib sequence. The function checks if `n` is 0, 1, or 2 and directly returns 0 in these cases. For larger values of `n`, it recursively computes the sum of the previous three terms in the sequence. This behavior is outlined in the docstring, which is accessible via the `__doc__` attribute of the function and also provides example usage and expected output.