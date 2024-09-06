```python
def fibfib(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    else:
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)
```
This function uses recursion to efficiently compute the n-th element of the FibFib sequence, adhering to the definition of the sequence. It handles the base cases (n = 0, n = 1) by returning 0, and for any other value of n, it recursively computes the sum of the previous three terms in the sequence.