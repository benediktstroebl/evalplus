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

# Tests
print(FibFib(1)[1])
# Output: 0

print(FibFib(5)[5])
# Output: 4

print(FibFib(8)[8])
# Output: 24
```

This script defines a custom sequence class `FibFib` that inherits from Python's built-in `Sequence` class, this allows the use of sequence-related methods such as `__getitem__` to index into the sequence and retrieve elements by index.

The `FibFib` class takes an `n` parameter which denotes the length of the FibFib sequence to create. During its initialization, it constructs the sequence by starting with the base cases (`fibfib(0) == 0`, `fibfib(1) == 0`, `fibfib(2) == 1`) and then iteratively calculating subsequent elements based on the defining formula `fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3)`.

The `__getitem__` method allows us to access elements of the sequence using index notation, such as `FibFib(1)[1]`. 

The provided test cases demonstrate how to use the class correctly, they verify that the first, fifth, and eighth elements of the FibFib sequence are indeed 0, 4, and 24 respectively.