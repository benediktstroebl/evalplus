from typing import List
def fibfib_helper(n: int, memo: List[int] = None) -> int:
    if n < 0:
        raise ValueError("FibFib is only defined for non-negative integers.")
    
    if memo is None:
        memo = [0, 0, 1]
        for i in range(3, n + 1):
            memo.append(memo[i - 1] + memo[i - 2] + memo[i - 3])
    
    return memo[n]
def fibfib(n: int) -> int:
    return fibfib_helper(n)