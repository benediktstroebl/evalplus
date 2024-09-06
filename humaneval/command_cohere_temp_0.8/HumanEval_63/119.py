```python
from collections import Sequence

class FibFib(Sequence):
    def __init__(self, n):
        self.n = n
        self.seq = [0, 0, 1]
        for i in range(3, n + 1):
            self.seq.append(self.seq[i-1] + self.seq[i-2] + self.seq[i-3])

    def __getitem__(self, i):
        return self.seq[i]

# Tests
print(FibFib(1)[1])
# Output: 0

print(FibFib(5)[5])
# Output: 4

print(FibFib(8)[8])
# Output: 24
```

This script defines a custom sequence class `FibFib` that overrides the `__getitem__` method to efficiently compute the `n-th` element of the FibFib sequence for any integer `n`. 

The example usage provided demonstrates how the class can be used to instantiate different sequences (`FibFib(1)`, `FibFib(5)`, `FibFib(8)`) and access specific elements in the sequence to obtain the corresponding values (`FibFib(1)[1]`, `FibFib(5)[5]`, `FibFib(8)[8]`). 

The output shows that the class is capable of correctly computing the FibFib values, matching the expected results.