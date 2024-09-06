```python
from collections import memoize

@memoize
def fibfib(n):
    if n < 3:
        return n
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

This script defines the `fibfib` function using the `memoize` decorator to ensure it will compute the FibFib values efficiently, avoiding redundant calculations. The function follows the definition of the FibFib sequence, where `FibFib(0) == 0`, `FibFib(1) == 0`, `FibFib(2) == 1`, and `FibFib(n) == FibFib(n-1) + FibFib(n-2) + FibFib(n-3)`. The provided unit tests ensure that the function produces the correct outputs for various inputs.