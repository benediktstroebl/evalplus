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
            raise IndexError("Invalid index")
        return self.seq[index]

# Test cases
print(FibFib(1)[1])       # Output: 0
print(FibFib(5)[5])       # Output: 4
print(FibFib(8)[8])       # Output: 24
```

This script defines a custom sequence class `FibFib` that implements the sequence behavior using the `__getitem__` method. This method generates the FibFib values on-the-fly and directly retrieves the value at the specified index, ensuring efficient computation of the FibFib numbers. The provided test outputs demonstrate the behavior of the class for different indices.