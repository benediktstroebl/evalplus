from typing import Optional
def fibfib(n: int, memo: Optional[dict] = None) -> int:
    if n < 0:
        raise ValueError("fibfib is not defined for negative numbers")
    
    if memo is None:
        memo = {}
    
    if n in memo:
        return memo[n]
    
    if n == 0:
        result = 0
    elif n == 1:
        result = 0
    else:
        result = fibfib(n-1, memo) + fibfib(n-2, memo) + fibfib(n-3, memo)
    
    memo[n] = result
    return result