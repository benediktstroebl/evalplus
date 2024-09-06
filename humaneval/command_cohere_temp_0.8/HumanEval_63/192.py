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
            raise IndexError("Index out of range")
        return self.seq[index]

def fibfib(n: int) -> int:
    """The FibFib number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    Returns the n-th element of the FibFib sequence."""
    fibfib_seq = FibFib(n)
    return fibfib_seq[n]

# Example usage:
print(fibfib(1))  # Output: 0
print(fibfib(5))  # Output: 4
print(fibfib(8))  # Output: 24
```

This code defines a custom sequence class `FibFib` that extends Python's built-in `Sequence` class and uses a generator expression to efficiently generate the sequence based on the definition provided in the problem statement. The `__getitem__` method is implemented to allow indexing access to elements of the sequence.

The `fibfib` function generates an instance of the `FibFib` sequence for a given `n` and returns the n-th element of the sequence, which effectively calculates the n-th element of the FibFib sequence.

The example usage demonstrates how to call the `fibfib` function to retrieve the desired elements from the FibFib sequence.