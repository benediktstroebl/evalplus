```python
def fibfib(n: int):
    if n < 0:
        raise ValueError("FibFib sequence is not defined for negative numbers")
    elif n == 0 or n == 1:
        return 0
    else:
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)
```
This code defines a recursive function that computes the n-th number in the FibFib sequence. The function firstly checks if `n` is equal to 0 or 1, in which case it returns 0. If `n` is less than 0, it raises a `ValueError` as the FibFib sequence is not defined for negative numbers. Otherwise, it returns the sum of the previous three elements in the sequence, achieved by recursively calling the function with arguments `n-1`, `n-2`, and `n-3`.