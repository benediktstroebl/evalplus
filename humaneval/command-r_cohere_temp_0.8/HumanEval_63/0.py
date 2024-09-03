```python
def fibfib(n):
    """Computes the n-th element of the fibfib number sequence:
    fibfib(0) = 0
    fibfib(1) = 0
    fibfib(2) = 1
    fibfib(n) = fibfib(n-1) + fibfib(n-2) + fibfib(n-3)
    """
    if n <= 1:
        return n
    elif n == 2:
        return 1
    # The offset FibFib sequence starts with 0, 0, 1, so the actual index is n - 3.
    fibs = [0, 0, 1]
    for i in range(3, n + 1):
        fibs.append(fibs[i - 1] + fibs[i - 2] + fibs[i - 3])
    return fibs[n]
```