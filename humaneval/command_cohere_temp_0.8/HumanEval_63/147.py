```python
from typing import Optional

def fibfib(n: int, memo: Optional[dict] = None) -> int:
    if n < 0:
        raise ValueError("FibFib is only defined for non-negative integers")
    if n == 0:
        return 0
    if n == 1:
        return 0
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    m1 = fibfib(n - 1, memo)
    m2 = fibfib(n - 2, memo)
    memo[n] = m1 + m2 + m1 + m2
    return memo[n]
```
This code defines a recursive function fibfib that computes the n-th FibFib number efficiently. It utilizes a memoization strategy to avoid redundant computations. The function checks if the results for smaller values of n are already in the memoization cache (a dictionary). If they are, it retrieves those results and avoids recalculating them. If n is 0 or 1, the function directly returns 0 since these are the base cases of the FibFib sequence. Otherwise, it recursively calculates the FibFib numbers for n-1 and n-2, adds them together twice (as per the definition of FibFib), and stores the result in the memoization dictionary before returning it. This approach helps optimize the computation and significantly reduces the number of recursive calls.