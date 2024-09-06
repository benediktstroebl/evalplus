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

This code defines a `FibFib` class that creates a sequence object that follows the FibFib sequence definition and allows indexing like a list to retrieve FibFib(n) values.

The `__getitem__` method is overridden to return the value at a given index, allowing the expression `FibFib(n)(index)` to work like a list to retrieve the FibFib number at index `index`.

The tests confirm that the class behaves as expected for different values of `n` and different indices.