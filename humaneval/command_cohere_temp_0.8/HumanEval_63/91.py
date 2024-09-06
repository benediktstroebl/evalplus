```python
from collections import Sequence

class FibFib(Sequence):
    def __init__(self, n):
        self.n = n
        self.seq = [0, 0, 1]
        for i in range(3, n + 1):
            self.seq.append(self.seq[i-1] + self.seq[i-2] + self.seq[i-3])

    def __getitem__(self, index):
        return self.seq[index]

# Test cases
assert FibFib(1)(0) == 0
assert FibFib(1)(1) == 0
assert FibFib(1)(2) == 1

assert FibFib(5)(4) == 5
assert FibFib(5)(5) == FibFib(5)(4) + FibFib(5)(3) + FibFib(5)(2)

assert FibFib(8)(7) == 21
assert FibFib(8)(8) == 24
```

The code defines a custom sequence class `FibFib` that implements the `Sequence` interface to enable appending and indexing operations. The `__init__` method initializes the sequence with the first three elements and generates subsequent elements using the definition of the FibFib sequence. The `__getitem__` method allows indexing the sequence like a list to retrieve specific elements. Test cases are included to validate the correctness of the class's implementation by checking if it produces the expected outputs for various input values.  This approach allows for efficient computation of the n-th element of the FibFib sequence and maintains a clean, understandable implementation.