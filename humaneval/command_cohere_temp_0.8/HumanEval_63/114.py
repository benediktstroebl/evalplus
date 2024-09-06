```python
def fibfib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    else:
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)
```
This function uses recursion to efficiently compute the n-th element of the FibFib sequence, as per the problem statement.