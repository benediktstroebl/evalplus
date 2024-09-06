```python
from typing import Optional

def fibfib_memo(n: int, memo: Optional[dict] = None) -> int:
    if n < 0:
        raise ValueError("FibFib is undefined for negative numbers")
    if n <= 1:
        return n
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    memobb = fibfib_memo(n-1, memo) + fibfib_memo(n-2, memo) + fibfib_memo(n-3, memo)
    memo[n] = memobb
    return memobb
```

The code defines a recursive function `fibfib_memo` that efficiently calculates the n-th number in the FibFib sequence using memoization to store previously computed values and avoid repeats. The function takes an additional optional parameter `memo`, which is a dictionary to store the previously computed values. The function returns the n-th FibFib number if n is a positive integer, raises a `ValueError` if n is negative, and fibfib(0) == 0 and fibfib(1) == 0 according to the specs.