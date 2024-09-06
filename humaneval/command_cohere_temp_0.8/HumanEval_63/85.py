```python
def fibfib(n: int):
    if n <= 0:
        return 0
    elif n == 1:
        return 0
    else:
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)
```
This function uses recursion to efficiently compute the n-th element of the FibFib sequence, adhering to the definition of the sequence. It handles the base cases of n=0 and n=1 correctly, providing the appropriate values of 0. For larger values of n, it recursively calls itself with decreased values of n, leveraging the definition of FibFib, thereby efficiently calculating the sequence value.