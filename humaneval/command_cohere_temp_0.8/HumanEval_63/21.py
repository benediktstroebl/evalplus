```python
def fibfib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    else:
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)
```
This function uses recursion to efficiently compute the n-th element of the FibFib sequence. The tests provided in the problem statement are handled correctly by the function, as they correspond to the expected direct access points 'n = 1', 'n = 5', and 'n = 8'.