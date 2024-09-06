```python
from collections import Sequence

def fibfib_sequence(n: int):
    """Returns nth value of the FibFib sequence"""
    base_cases = [0, 0, 1]
    if n < 3:
        return base_cases[n]
    else:
        thresh = 10**5
        memo = [None] * (thresh + 1)
        for i in range(3, n + 1):
            memo[i] = memo[i - 1] + memo[i - 2] + base_cases[i - 3]
        return memo[n]

# Test cases
assert fibfib_sequence(1) == 0
assert fibfib_sequence(5) == 4
assert fibfib_sequence(8) == 24
```

This script defines the `fibfib_sequence` function, which returns the n-th value in the FibFib sequence, and uses memoization to ensure efficiency. Additionally, it includes test cases to validate the function's correctness. You can use the function by calling `fibfib_sequence(n)` with the desired value of `n`. 

Let me know if you would like me to explain any part of the code in more detail.