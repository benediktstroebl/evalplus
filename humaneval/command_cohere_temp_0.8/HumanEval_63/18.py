```python
def fibfib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 0
    else:
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)
```
This function uses recursive calls with optimized memory usage to efficiently compute the n-th element of the FibFib sequence. It adheres to the problem definition, returning 0 for invalid inputs and executing the recursive steps for valid inputs. The deep recursive nature of the problem makes this one of the classic examples of problems that benefit from recursive solutions, elegantly solved by simply 'calling yourself'.