```python
from typing import List

def fibfib_list(n: int) -> List[int]:
    fibfib = [0, 0, 1]
    while len(fibfib) <= n:
        fibfib.append(fibfib[-1] + fibfib[-2] + fibfib[-3])
    return fibfib

def fibfib(n: int) -> int:
    return fibfib_list(n)[-1]

# Unit tests:
print(fibfib(1))
# Should print: 0

print(fibfib(5))
# Should print: 4

print(fibfib(8))
# Should print: 24
```

This script defines a function `fibfib` that efficiently calculates the n-th element of the FibFib sequence specified in the problem statement. It does this by iterating through the sequence and building a list of FibFib numbers in a loop, which is more efficient than the naive recursive approach that would be prone to recursion limit errors for larger values of n.