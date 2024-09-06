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
This code defines a recursive function `fibfib` that calculates the n-th number in the FibFib sequence, a variant of the Fibonacci sequence. The function starts with basic cases `n=0`, `n=1`, and `n=2` that return the corresponding sequence values directly. For larger `n`, the function recursively computes the current number by summing the three previous values in the sequence, as defined by the sequence's definition `fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3)`.