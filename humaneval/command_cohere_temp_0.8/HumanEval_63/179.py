```python
def fibfib(n: int):
    if n <= 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)
```
This function uses a recursive approach to compute the n-th element of the FibFib sequence, following the definition of the sequence. It handles the base cases of n=0, n=1, and n=2, and recursively calls itself for larger values of n, always combining the results of the previous three terms in the sequence.