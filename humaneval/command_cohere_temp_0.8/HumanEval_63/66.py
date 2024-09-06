```python
from typing import List

def fibfib_list(n: int) -> List[int]:
    fibfib = [0, 0, 1]
    while len(fibfib) <= n:
        fibfib.append(sum(fibfib[-3:] + [fibfib[-1]]))
    return fibfib

def fibfib(n: int) -> int:
    return fibfib_list(n)[-1]

# Tests
assert fibfib(1) == 0
assert fibfib(5) == 4
assert fibfib(8) == 24
```

The function `fibfib_list` computes the FibFib sequence up to `n` and returns the list representing the sequence. This is done efficiently in a single pass. The function `fibfib` is a wrapper that provides a direct way to get the n-th element of the sequence without having to compute the full sequence upfront.