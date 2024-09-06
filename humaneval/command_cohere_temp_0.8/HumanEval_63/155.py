```python
from collections import Sequence

def fibfib_iter(n: int, memo: Sequence = None):
    if n < 0:
        raise ValueError("FibFib is only defined for non-negative integers")
    if n == 0:
        return 0
    if n == 1:
        return 0
    if memo is None:
        memo = []
    if n in memo:
        return memo[n]
    memo[n] = fibfib_iter(n - 1, memo) + fibfib_iter(n - 2, memo) + fibfib_iter(n - 3, memo)
    return memo[n]

def fibfib(n: int):
    return fibfib_iter(n)

# Tests
assert fibfib(0) == 0
assert fibfib(1) == 0
assert fibfib(2) == 1
assert fibfib(5) == 4
assert fibfib(8) == 24
```

This code defines two functions: `fibfib_iter` uses an iterative approach and maintains a memoization cache, while `fibfib` directly calls `fibfib_iter` to compute the n-th FibFib number. The tests demonstrate the behavior of the functions for different input values.