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
    if n < 3:
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)
    else:
        val = fibfib(n-1, memo) + fibfib(n-2, memo) + fibfib(n-3, memo)
        if memo is not None:
            memo[n] = val
        return val