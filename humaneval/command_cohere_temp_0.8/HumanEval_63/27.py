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
This function implements the definition of the FibFib sequence, where `FibFib(0) == 0`, `FibFib(1) == 0`, `FibFib(2) == 1` and `FibFib(n) == FibFib(n-1) + FibFib(n-2) + FibFib(n-3)`. It uses recursive calls to efficiently compute the n-th element of the FibFib number sequence. However, please note that due to its exponential growth nature, the FibFib sequence's larger values may quickly become too large for the Python integer data type to handle. In such cases, you may need to consider using specialized data types for handling large integers or considering alternative approaches like memoization to prevent redundant calculations.