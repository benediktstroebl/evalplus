# CANNOT PARSE CODE SNIPPET
python
def fibfib(n: int) -> int:
    """Compute the n-th element of the FibFib number sequence."""
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b, c = 0, 0, 1
        for i in range(2, n):
            a, b, c = b, c, a + b + c
        return a + b + c
