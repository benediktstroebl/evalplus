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
This code defines the `fibfib` function, which is a recursive function that calculates the n-th number in the FibFib sequence, which is a variation of the Fibonacci sequence. The function first checks if `n` is less than or equal to 0, in which case it returns 0. If `n` is 1, it also returns 0. If `n` is 2, it returns 1. For all other values of n, the function returns the sum of the previous three terms in the sequence, recursively calling `fibfib` as necessary.