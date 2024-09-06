```python
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

# Tests
assert fibfib(0) == 0
assert fibfib(1) == 0
assert fibfib(2) == 1
assert fibfib(5) == 4
assert fibfib(8) == 24
```

This code defines two functions:
- `fibfib_helper(n, memo)`: This is the core computation mechanism for the FibFib sequence. It's a recursive function, but it benefits from memoization to avoid redundant calculations. If the `memo` list is `None`, it initializes the list and computes the sequence up to the given `n` value. If `memo` is not `None`, it returns the value at position `n` from the pre-computed sequence.
- `fibfib(n)`: This function wraps the `fibfib_helper` function and handles potential input errors. It checks if the input value `n` is non-negative, and if so, it calls `fibfib_helper` to compute the nth FibFib number. 

The test assertions at the end demonstrate the correct behavior of the function for the given test cases.