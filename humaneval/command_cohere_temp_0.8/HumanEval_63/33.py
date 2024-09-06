```python
def fibfib(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    else:
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)
```
This function implements the definition of the FibFib sequence, where FibFib(0) and FibFib(1) both equal 0, and FibFib(n) equals the sum of the previous three sequence elements for any positive integer value of n. It does so in an efficient manner using a recursive approach.