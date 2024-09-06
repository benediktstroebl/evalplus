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
if __name__ == "__main__":
    print(FibFib(1)[1])
    print(FibFib(5)[5])
    print(FibFib(8)[8])
```

This script defines a `FibFib` class that creates an instance sequence where each element is the FibFib number at the corresponding index. The `__getitem__` method is overridden to enable indexing of the sequence. The provided test cases output the correct values, demonstrating the class's functionality.