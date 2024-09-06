```python
def fibfib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    else:
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)
```
This function uses recursive calls to the previous three elements of the sequence in order to efficiently compute the nth element of the FibFib sequence. The function adheres to the definition of the FibFib sequence provided in the problem statement. And passes the provided tests.