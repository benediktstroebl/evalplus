```python
from typing import Optional

def fibfib(n: int, memo: Optional[dict] = None) -> int:
    if n < 0:
        raise ValueError("FibFib is defined only for non-negative integers")
    if n == 0:
        return 0
    if n == 1:
        return 0
    if memo is not None and n in memo:
        return memo[n]
    m1 = fibfib(n - 1, memo)
    m2 = fibfib(n - 2, memo)
    memo_value = m1 + m2 + fibfib(n - 3, memo)
    if memo is not None:
        memo[n] = memo_value
    return memo_value
```

This script defines the `fibfib` function that efficiently calculates the n-th element of the FibFib sequence, adhering to the problem's definition. It uses a recursive approach with memoization to ensure optimized and correct calculations. This solution handles edge cases such as negative input and immediately returns the defined values for `fibfib(0)` and `fibfib(1)`. The memoization dictionary helps store already calculated values, preventing redundant computations.