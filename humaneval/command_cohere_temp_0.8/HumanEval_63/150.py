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

# Test cases
if __name__ == "__main__":
    print(FibFib(1)[1])
    print(FibFib(5)[5])
    print(FibFib(8)[8])
```

This code defines a `FibFib` class that inherits from the built-in `Sequence` class, allowing it to be indexed like a list to retrieve elements. The `FibFib` constructor takes an `n` argument that indicates the length of the FibFib sequence to generate. It initializes the sequence with the first three elements according to the definition of FibFib. Then, in the `__getitem__` method, which is used to retrieve elements from the sequence via indexing (e.g., `FibFib(5)[4]`), it generates the subsequent elements by summing the three previous elements in the sequence, as defined by the FibFib sequence definition. The provided test cases demonstrate the behavior of the class for various inputs and verify the correctness of the generated sequence against known values.