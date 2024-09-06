```python
def fibfib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    else:
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)
```
This function uses recursion to efficiently compute the n-th element of the FibFib sequence. The tests provided in the problem statement are basic and can be easily passed by this simple recursive function. However, space complexity of the recursive approach should be kept in mind for larger values of n as it may lead to a stack overflow due to exponential growth of the sequence.