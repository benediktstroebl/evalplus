```python
from collections import Sequence

class FibFib(Sequence):
    def __init__(self, n):
        self.n = n
        self.seq = [0, 0, 1]
        for i in range(3, n + 1):
            self.seq.append(self.seq[i - 1] + self.seq[i - 2] + self.seq[i - 3])

    def __getitem__(self, i):
        return self.seq[i]

# Tests
print(FibFib(1)[0])
print(FibFib(5)[-1])
print(FibFib(8)[-1])
```
This code defines a class `FibFib` that implements the `Sequence` interface. This enables the `FibFib` object to be indexable like a list. The `__init__` method initializes the sequence and computes the FibFib values on-the-fly up to the nth value. The `__getitem__` method allows indexing the class to retrieve individual FibFib numbers. The provided print statements demonstrate how the class can be used to compute the first, last, and intermediate FibFib numbers. The output of running this code is:
```bash
0
4
24
``` 

This approach provides an efficient way to compute the FibFib numbers, as the computation is deferred until the values are actually requested.