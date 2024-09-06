from typing import Optional
def fibfib(n: int, memo: Optional[dict] = None) -> int:
    if n < 0:
        raise ValueError("FibFib is defined only for non-negative integers")
    
    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 1
    
    if memo is None:
        memo = {}
    
    # Check if the solution to the n-th FibFib number is already computed and stored in the memo dictionary
    if n in memo:
        return memo[n]
    
    # Otherwise, compute the n-th FibFib number iteratively by summing the previous 3 elements in the sequence
    memo[n] = fibfib(n - 1, memo) + fibfib(n - 2, memo) + fibfib(n - 3, memo)
    return memo[n]