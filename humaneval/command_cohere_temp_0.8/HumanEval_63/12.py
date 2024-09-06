```python
def fibfib(n: int):
    if n < 0:
        raise ValueError("FibFib sequence is not defined for negative numbers")
    elif n < 3:
        return n == 0 or n == 1 ? 0 : 1
    else:
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)
```
This code defines a recursive function `fibfib` that computes the n-th number in the FibFib sequence. It starts by checking for edge cases: if n is negative, it raises a ValueError, and if n is 0, 1, or 2, it directly returns 0 or 1 accordingly. For larger n, it recursively calls itself with n-1, n-2, and n-3, adding the results to compute the n-th FibFib number.