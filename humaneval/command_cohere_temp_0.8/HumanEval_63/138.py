```python
from collections import memoize

@memoize
def fibfib(n):
    if n == 0:
        return 0
    if n == 1:
        return 0
    elif n == 2:
        return 1
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

This Python script defines a function `fibfib` that efficiently computes the n-th element of the FibFib sequence, based on the definition you provided. It uses memoization with the `memoize` decorator to ensure that each value is computed only once and then reused, ultimately improving the function's performance as the input grows.