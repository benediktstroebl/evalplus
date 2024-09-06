```python
def fibfib(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    else:
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)
```
This function uses recursion to efficiently compute the n-th element of the FibFib sequence. Each function call reduces the problem size by 3 (essentially computing the sum of the previous 3 elements in the sequence), which is a common technique used in dynamic programming to efficiently compute recursive sequences like these.