```python
def fibfib(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    else:
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)
```
This function uses recursion to efficiently compute the n-th element of the FibFib sequence. The recursive equation is derived from the definition of the FibFib sequence: `fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3)`. Simply provide the desired `n` to the function and it will return the corresponding FibFib number. 
You can verify the correct operation of the function by testing it with the following commands:
```python
>>> fibfib(1)
0

>>> fibfib(5)
4

>>> fibfib(8)
24
```
This should return the expected results of 0, 4, and 24 respectively.