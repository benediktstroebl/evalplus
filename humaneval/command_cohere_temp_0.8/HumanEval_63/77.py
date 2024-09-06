```python
from itertools import accumulate

def fibfib_iter(n: int):
    if n < 0:
        raise ValueError("FibFib is only defined for non-negative integers.")
    fib = [0, 0, 1]
    for i in range(3, n + 1):
        fib.append(fib[i-1] + fib[i-2] + fib[i-3])
    return accumulate(fib)[-1]

# Tests
assert fibfib_iter(1) == 0
assert fibfib_iter(5) == 4
assert fibfib_iter(8) == 24
```
This code defines the `fibfib_iter` function, which calculates the n-th FibFib number efficiently using a generator expression and the `accumulate` function to avoid redundant calculations. This iteration-based approach differs from the more common recursive approach, which can lead to performance issues for larger values of n due to excessive function calls.