```python
def fibfib(n: int):
    if n < 0:
        raise ValueError("FibFib sequence is not defined for negative numbers")
    elif n < 3:
        return n == 0 or n == 1  # Special cases
    else:
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)
```

This script defines a recursive function `fibfib` that efficiently calculates the n-th element of the FibFib sequence, handling exceptions for negative input or input that is less than 3. Simply provide a number n to the function to get the corresponding FibFib value.