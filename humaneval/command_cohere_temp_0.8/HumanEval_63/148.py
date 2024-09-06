```python
from typing import List

def fibfib_memo(n: int, memo: List[int] = None) -> int:
    if n < 0:
        raise ValueError("FibFib is undefined for negative numbers")
    if n <= 1:
        return n
    if memo is None:
        memo = [0, 0]
    if n <= len(memo):
        return memo[n]
    memo_len = len(memo)
    memo[memo_len] = fibfib_memo(n - 1, memo) + fibfib_memo(n - 2, memo) + memo[memo_len - 1]
    return memo[memo_len]
```

The function has two parameters:
- `n`: The index of the desired FibFib number.
- `memo`: An optional list that remembers the already computed FibFib numbers. This parameter is used for efficient recursive computation, avoiding redundant calculations.

This implementation avoids redundant calculations by storing computed values in the `memo` list, recursively passing this list through the computation. The base cases are `n=0` and `n=1`, which are both 0, and the recursive case is `n-1` and `n-2` for the previous two values in the sequence.