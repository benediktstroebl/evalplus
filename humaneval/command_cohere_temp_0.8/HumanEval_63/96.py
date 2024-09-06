```python
from functools import lru_cache

@lru_cache(None)
def fibfib(n: int):
    if n < 0:
        raise ValueError("FibFib sequence is not defined for negative numbers.")
    elif n <= 2:
        return n == 0
    else:
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)
```

This script defines the `fibfib` function using a decorator from the `functools` module called `lru_cache`. This decorator caches the results of method calls, accelerating consecutive calls for the same input values. The function checks if the input `n` is negative, and if so, raises a `ValueError` as the FibFib sequence is not defined for negative numbers. If `n` is 0 or 1, the function returns 0 since these are the first elements of the sequence. For n > 2, it invokes the cached function calls recursively for `n-1`, `n-2`, and `n-3`, and returns their sum, in accordance with the definition of the FibFib sequence.

Cache memory usage can be customized using the `lru_cache` decorator's optional arguments. The `maxsize` argument defines the maximum number of recent calls to cache, and the `typed` argument, which is set to `True` by default, caches each distinct type of input.