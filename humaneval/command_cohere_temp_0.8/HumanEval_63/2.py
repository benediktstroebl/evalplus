```python
def fibfib(n: int):
    if n < 0:
        raise ValueError("FibFib sequence is not defined for negative numbers")
    elif n < 3:
        return n
    else:
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)
```
This code defines a recursive function fibfib that computes the n-th number in the FibFib sequence. The function first checks if n is less than 3 (the base cases), returning 0 or 1 for n=0,1 and raising a ValueError for negative input. If n is greater than or equal to 3, the function recursively calls itself to compute the nth FibFib number by summing the previous three elements in the sequence.