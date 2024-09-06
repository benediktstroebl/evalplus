```python
def fibfib(n: int):
    if n < 0:
        raise ValueError("FibFib sequence is not defined for negative numbers")
    elif n == 0 or n == 1:
        return 0
    else:
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)
```
This code defines a recursive function fibfib that computes the n-th number in the FibFib sequence. The function first checks if n is equal to 0 or 1, in which case it returns 0. If n is greater than 1, the function recursively calls itself to calculate the sums of the (n-1)-th, (n-2)-th, and (n-3)-th terms in the sequence, and returns the sum. Also, the function includes a check for negative input, and raises a ValueError if the input is negative, as the FibFib sequence is not defined for negative numbers.