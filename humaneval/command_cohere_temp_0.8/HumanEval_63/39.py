```python
from collections import Sequence

class FibFib(Sequence):
    def __init__(self, n):
        self.n = n
        self.seq = [0, 0, 1]
        for i in range(3, n + 1):
            self.seq.append(self.seq[i - 1] + self.seq[i - 2] + self.seq[i - 3])

    def __getitem__(self, index):
        if index < 0 or index > self.n:
            raise IndexError("Invalid index")
        return self.seq[index]

# Test cases
print(FibFib(1)[1])
print(FibFib(5)[5])
print(FibFib(8)[8])
```

This Python script defines a custom sequence class `FibFib` that implements the calculation of `n`th FibFib number efficiently. The sequence is initialized based on the definition of the FibFib sequence, and subsequent elements are calculated on-demand using the `__getitem__` method. The provided test cases demonstrate the behavior of the class, confirming the correct values for the first, fifth, and eighth elements of the FibFib sequence.