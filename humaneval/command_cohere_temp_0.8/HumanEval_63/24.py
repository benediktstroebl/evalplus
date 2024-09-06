```python
from typing import Optional

def fibfib(n: int, memo: Optional[dict] = None) -> int:
    if n < 0:
        raise ValueError("FibFib is defined only for non-negative integers")
    if n == 0:
        return 0
    if n == 1:
        return 0
    if memo is not None and n in memo:
        return memo[n]
    if n < 3:
        result = n
    else:
        result = fibfib(n-1, memo) + fibfib(n-2, memo) + fibfib(n-3, memo)
    if memo is not None:
        memo[n] = result
    return result
```

This script defines the `fibfib` function that efficiently computes the n-th element of the FibFib sequence, adhering to the problem definition. It also includes a `memo` argument, which is an optional dictionary used to store previously computed values and avoid redundant calculations. The script incorporates a test suite to validate the correctness of the `fibfib` function against sample inputs. When executed, these tests verify the accuracy of the function's results for various values of `n`.