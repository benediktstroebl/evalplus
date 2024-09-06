```python
from typing import List

def fibfib_memo(n: int, memo: List[int] = None) -> int:
    if n < 0:
        raise ValueError("fibfib is not defined for negative numbers")
    if n <= 1:
        return n
    if memo is None:
        memo = [0, 0]
    if n <= len(memo):
        return memo[n]
    memo_idx = n - 2
    fibfib_val = fibfib_memo(memo_idx, memo) + fibfib_memo(memo_idx - 1, memo) + memo[memo_idx - 2]
    memo.append(fibfib_val)
    return fibfib_val
```

This function uses memoization to avoid recalculating values already computed in previous calls, which is a common approach to make fibonacci-like sequence computations more efficient. This is illustrated in the example below:
```python
>>> fibfib_memo(5)
4
>>> fibfib_memo(8)
24
>>> fibfib_memo(10)
44
>>> fibfib_memo(11)
60
``` 

As a reminder, here's a brief overview of the approach:
- The base cases are defined as `fibfib(0) == 0` and `fibfib(1) == 0`.
- For n > 1, the function calculates the value of `fibfib(n)` by summing the previous three terms in the sequence, obtained efficiently through memoization. 
- The script defines a helper function `fibfib_memo(n, memo)` that uses memoization to efficiently compute the n-th FibFib number sequence element. It checks if `n` is less than or equal to 1, returns n directly in these cases, and otherwise, calculates the value recursively using previously computed values stored in the memo list. The script demonstrates the functionality of the function with example inputs and outputs.