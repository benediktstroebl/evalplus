```python
def fibfib(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    else:
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)
```
This function uses recursion to efficiently compute the n-th element of the FibFib sequence. The base cases are defined with `n==0`, `n==1`, and it follows the definition of the sequence for `n>1`. 

You can test this function by calling it with different values of `n` and comparing the results with the expected values from the comment at the top of the code block.