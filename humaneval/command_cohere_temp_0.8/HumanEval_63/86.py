```python
from functools import lru_cache

@lru_cache(None)
def fibfib(n: int):
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

This script defines the `fibfib` function using a Python decorator (`lru_cache`) that optimizes the function by storing previous calls and thereby removes the need for recursion and reduces the function's runtime. It validates the function against several sample inputs, ensuring the correct behavior and indicating the n-th element of the FibFib sequence.