from collections import memoizemodule
def fibfib(n: int, memo = {}):
    if n < 0:
        raise ValueError("FibFib is only defined for non-negative integers.")
    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 1
    
    if n in memo:
        return memo[n]
    
    memo[n] = fibfib(n-1, memo) + fibfib(n-2, memo) + fibfib(n-3, memo)
    return memo[n]