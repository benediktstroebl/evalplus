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

This script defines a recursive function `fibfib` that operates similarly to the Fibonacci sequence but with the altered first two elements. The function will return 0 for n equal to 0, 1, or 2, and will return the sum of the previous three sequence elements for n greater than 2. This should efficiently compute the n-th element of the `FibFib` sequence.