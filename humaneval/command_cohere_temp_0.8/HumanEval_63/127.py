```python
from collections import Sequence

class FibFib(Sequence):
    def __init__(self, n):
        self.n = n
        self.seq = [0, 0, 1]
        for i in range(3, n + 1):
            self.seq.append(self.seq[i - 1] + self.seq[i - 2] + self.seq[i - 3])

    def __getitem__(self, index):
        if index < self.n:
            return self.seq[index]
        else:
            raise IndexError()

def fibfib(n: int):
    """The FibFib number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    Please write a function to efficiently compute the n-th element of the fibfib number sequence.
    >>> fibfib(1)
    0
    >>> fibfib(5)
    4
    >>> fibfib(8)
    24
    """
    return FibFib(n)][n - 1]
```

This code defines a `FibFib` class that encapsulates the FibFib sequence, and uses the `__getitem__` method to allow indexing like a list. The `fibfib` function then initializes a `FibFib` instance and returns the n-th value from it. This approach makes use of Python's sequence protocol and allows the efficient computation of the FibFib values.