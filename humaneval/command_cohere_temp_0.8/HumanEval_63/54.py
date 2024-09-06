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

This script defines a recursive function `fibfib` that matches the definition of the FibFib sequence provided in the prompt. The function takes an integer `n` as input and returns the n-th number in the FibFib sequence. It implements recursive checks for the base cases (`n<=0`, `n==1`, and `n==2`) and then calls the function recursively for `n-1`, `n-2`, and `n-3` to compute the n-th FibFib number.