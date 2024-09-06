```python
def fibfib(n: int):
    if n < 0:
        raise ValueError("FibFib sequence is not defined for negative numbers")
    elif n == 0 or n == 1:
        return 0
    else:
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)
```
This code defines a recursive function that computes the n-th number in the FibFib sequence. It first checks if n is equal to 0 or 1, in which case it returns 0. If n is greater than 1, it recursively calls the function with n-1, n-2, and n-3 and adds the results together. This effectively calculates the n-th FibFib number in a manner similar to the Fibonacci sequence.