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