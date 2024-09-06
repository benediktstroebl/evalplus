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