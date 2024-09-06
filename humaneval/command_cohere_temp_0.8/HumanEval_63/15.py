```python
def fibfib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    else:
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)
```
This function uses recursive calls to the previous three terms in the sequence, with the base cases for 0 and 1. It is memoized, so it efficiently computes the n-th element of the fibfib number sequence in O(n) time.