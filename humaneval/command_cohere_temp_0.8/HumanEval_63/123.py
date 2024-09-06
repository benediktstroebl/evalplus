```python
from itertools import accumulate

def fibfib_iter(n):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    else:
        a, b, c = 0, 1, 0
        for i in range(2, n+1):
            a, b, c = b, a + b + c, c
        return a

def fibfib(n):
    return next(accumulate([0, 0, 1], fibfib_iter))[n]
```

The function `fibfib_iter` returns an iterator, which allows it to be used in a list comprehension, making it more memory-efficient as it doesn't need to store the entire sequence. The `fibfib` function uses the iterator (`fibfib_iter`) to generate the FibFib values and the `accumulate` function to calculate the final value for n.