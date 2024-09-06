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
This code defines a recursive function `fibfib` that computes the n-th number in the FibFib sequence. The function starts with two base cases (`n == 0` and `n == 1`) both of which return 0. The function returns 1 for `n == 2` as it is the third number in the sequence. For `n > 2`, the function recursively calls itself with arguments `n-1`, `n-2`, and `n-3` and adds up the results to compute the n-th FibFib number.