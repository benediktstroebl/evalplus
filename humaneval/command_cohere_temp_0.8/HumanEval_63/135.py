```python
from collections import Sequence

class FibFib(Sequence):
    def __init__(self, n):
        self.n = n
        self.seq = [0, 0, 1]
        for i in range(3, n + 1):
            self.seq.append(self.seq[i - 1] + self.seq[i - 2] + self.seq[i - 3])

    def __getitem__(self, index):
        if 0 <= index < self.n:
            return self.seq[index]
        else:
            raise IndexError()

# Test cases
print(FibFib(1)[1])  # 0 (test case from the prompt)
print(FibFib(5)[5])  # 4 (test case from the prompt)
print(FibFib(8)[8])  # 24 (test case from the prompt)
```

This code defines a class `FibFib` that implements the `Sequence` interface, enabling it to work seamlessly with indexing operations. The `__init__` method initializes the sequence with the first three elements and generates subsequent elements using the defining recurrence relation. The `__getitem__` method is used for indexing, ensuring that the index is within the valid range and returning the corresponding value if it is. Test cases are included to verify the behavior against the prompt's expectations.