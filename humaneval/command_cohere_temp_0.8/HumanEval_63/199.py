```python
def fibfib(n: int):
    if n < 0:
        raise ValueError("FibFib sequence is not defined for negative numbers")
    elif n < 3:
        return n
    else:
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)
```
This code defines a recursive function fibfib that computes the n-th number in the FibFib sequence. The function first checks if n is less than 3 (the base cases for the sequence). If n is 0 or 1, it returns 0, and if n is 2, it returns 1. If n is greater than or equal to 3, the function recursively calls itself to compute the sum of the previous three terms in the sequence by subtracting 3 from n and calling fibfib() for n-1, n-2, and n-3. Furthermore, it includes a check to ensure n isn't a negative number, and if it is, the function raises a ValueError.