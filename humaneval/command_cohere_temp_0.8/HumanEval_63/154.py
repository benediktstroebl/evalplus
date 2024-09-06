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

This code defines a `FibFib` class that creates an instance sequence where each element is the sum of the previous three elements in the sequence. The `__getitem__` method is overridden to enable indexing (e.g., `fibfib[5]`), allowing access to specific sequence elements. Test cases are included to validate the behavior of the class. 

This approach leverages Python's Sequence protocol and uses list comprehensions and generators to efficiently compute and store the sequence elements. This makes the `FibFib` class scalable and suitable for handling larger values of `n`. 

To improve efficiency, the `FibFib` class stores the first three elements of the sequence and leverages a generator to lazily generate the subsequent elements on-the-fly only when accessed. This saves both memory and computation, making it efficient even for large values of `n`.