```python
def fibfib(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    else:
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)
```
This function uses recursive calls to the previous three terms in the sequence to compute the next term efficiently. It is essentially a direct implementation of the defining formula. Note that this approach has an exponential time complexity, so it may not be suitable for large values of n. However, for small values of n (such as those cited in the example), it will work efficiently.