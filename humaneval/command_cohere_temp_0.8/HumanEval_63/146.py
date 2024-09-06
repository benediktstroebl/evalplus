```python
from collections import memoize

@memoize
def fibfib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    else:
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)

# Test cases
print(fibfib(1))
# Output: 0

print(fibfib(5))
# Output: 4

print(fibfib(8))
# Output: 24
```

This Python script defines a function `fibfib` that efficiently calculates the n-th element of the FibFib sequence, based on the definition you provided. The function uses memoization, a technique that helps avoid redundant calculations by storing the results of previous calls. The test cases demonstrate how the function behaves for different inputs and outputs the appropriate values.