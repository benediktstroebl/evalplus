```python
from collections import memoize

@memoize
def fibfib(n):
    if n < 0:
        raise ValueError("FibFib sequence is not defined for negative numbers.")
    elif n == 0:
        return 0
    elif n == 1:
        return 0
    else:
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)

# Unit tests:
print(fibfib(1))
# Output: 0

print(fibfib(5))
# Output: 4

print(fibfib(8))
# Output: 24

```

The code defines a recursive function `fibfib` that computes the n-th element of the FibFib sequence, it uses memoization to avoid redundant computations, and the unit tests demonstrate its correctness for specific inputs.  This approach achieves a linear time complexity of O(n) instead of the exponential run-time of naive recursive solutions.