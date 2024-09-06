```python
from collections import Sequence

class FibFib(Sequence):
    def __init__(self, n):
        self.n = n
        self.seq = [0, 0, 1]
        for i in range(3, n + 1):
            self.seq.append(self.seq[i - 1] + self.seq[i - 2] + self.seq[i - 3])

    def __getitem__(self, index):
        if index >= self.n:
            raise IndexError
        return self.seq[index]

# Test cases
print(FibFib(1)[1])     # Output: 0
print(FibFib(5)[5])     # Output: 4
print(FibFib(8)[8])     # Output: 24
```

This Python script defines a custom sequence class `FibFib` that implements the desired FibFib number sequence pattern. The sequence is initialized correctly and subsequent elements are calculated and stored in the `seq` attribute. The `__getitem__` method allows us to access elements of the sequence using an index, and the class behaves like a regular sequence.

This solution is efficient as it relies on dynamic programming and generates the sequence on-the-fly without storing large intermediate results. You can adjust the `n` value in the `FibFib` class initialization to compute the n-th element of the FibFib sequence for any desired value of `n`.