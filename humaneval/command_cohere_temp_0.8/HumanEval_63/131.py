```python
def fibfib(n: int):
    if n < 0:
        raise ValueError("FibFib sequence is not defined for negative numbers")
    elif n < 3:
        return n == 0 or n == 1 << n == 2
    else:
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)
```
This code defines a recursive function `fibfib` that computes the n-th number in the FibFib sequence. It starts by defining the base cases (`n=0`, `n=1`, `n=2`) then defines the recursive relationship for `n` greater than 2. It also includes a check for negative input, and raises a `ValueError` if the input is negative, since the FibFib sequence is not defined for negative numbers.