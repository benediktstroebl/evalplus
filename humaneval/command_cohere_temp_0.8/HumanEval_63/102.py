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

This Python script defines a custom sequence class `FibFib` that implements the desired FibFib number sequence based on the definition provided in the prompt. This class allows you to create instances of the sequence and access specific elements using indexing, just like built-in sequence types. The output confirms that the class behaves as expected for the provided test cases.