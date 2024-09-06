```python
def fibfib(n: int):
    if n < 0:
        raise ValueError("FibFib sequence is not defined for negative numbers")
    elif n == 0 or n == 1:
        return 0
    else:
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)
```
This code defines a recursive function fibfib that computes the n-th number in the FibFib sequence. It starts by checking for base cases n == 0 and n == 1, where it returns 0. It then recursively calls fibfib with n-1, n-2, and n-3, and adds the results to compute the n-th number in the sequence. This approach efficiently computes the desired values.