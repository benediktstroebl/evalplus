```python
def fibfib(n: int):
    if n < 0:
        raise ValueError("FibFib sequence is not defined for negative numbers")
    elif n == 0 or n == 1:
        return 0
    else:
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)
```
This code defines a recursive function fibfib that computes the n-th number in the FibFib sequence. It starts by checking for two base cases: n == 0 and n == 1, which both return 0. If n is not in these bases, it recursively calls fibfib(n-1) + fibfib(n-2) + fibfib(n-3) to compute the n-th FibFib number. It also includes a check for negative numbers, raising a ValueError if n is negative. This prevents the function from descending into infinite recursion for invalid inputs.