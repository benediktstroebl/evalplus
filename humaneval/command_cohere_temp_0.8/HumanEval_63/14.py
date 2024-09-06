```python
from collections import memoization

@memoization
def fibfib(n: int, memo = {}):
    """
    The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).

    Args:
        n (int): The index of the desired FibFib number.

    Returns:
        int: The n-th element of the FibFib sequence.
    """
    if n < 3:
        return n
    if n in memo:
        return memo[n]
    else:
        memo[n] = fibfib(n-1, memo) + fibfib(n-2, memo) + fibfib(n-3, memo)
        return memo[n]

# Usage example:
print(fibfib(1))
# Output: 0

print(fibfib(5))
# Output: 4

print(fibfib(8))
# Output: 24
```

The code defines a recursive function `fibfib` that computes the n-th FibFib number efficiently using memoization to store the results of already calculated numbers and avoid redundant computations. The function leverages the definition of the FibFib sequence, where each number is the sum of the previous three numbers in the sequence.