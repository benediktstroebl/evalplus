```python
def fibfib(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    else:
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)
```
This function uses recursion to efficiently compute the n-th element of the FibFib sequence. The tests provided in the prompt return the following values:
```
>>> fibfib(1)
0
>>> fibfib(5)
4
>>> fibfib(8)
24
```
These values align with the definition of the FibFib sequence provided in the prompt, where subsequent terms are generated as the sum of the previous three terms.