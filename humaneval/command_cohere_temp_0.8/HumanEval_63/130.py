```python
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

# Tests
print(fibfib(1))  # Output: 0
print(fibfib(5))  # Output: 4
print(fibfib(8))  # Output: 24
```

This Python script defines a function `fibfib` that efficiently computes the n-th element of the FibFib number sequence defined in the problem statement. The function uses a memoization technique to store previously computed values and avoid redundant calculations, enhancing performance for larger values of `n`. The tests provided in the problem statement are included and ensure the correct behavior of the function.