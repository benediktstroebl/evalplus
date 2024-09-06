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

This script defines a recursive function `fibfib` that operates on the `FibFib` sequence, which is closely related to the Fibonacci sequence. The function takes an integer `n` as input and returns the n-th number in the `FibFib` sequence. It provides base cases for 0 and 1, and for larger `n`, it recursively calculates the sum of the previous three terms in the sequence.