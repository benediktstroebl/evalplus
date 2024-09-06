```python
def fibfib(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    else:
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)
```
This function implements the definition of the FibFib sequence, where `FibFib(0) == 0`, `FibFib(1) == 0`, and `FibFib(n) == FibFib(n-1) + FibFib(n-2) + FibFib(n-3)`. It uses a recursive approach to calculate the sequence element using three previous sequence elements. The base cases `n==0` and `n==1` are returned explicitly, while for `n>1` it recursively calls itself with the arguments `n-1`, `n-2`, and `n-3` and adds up the results.