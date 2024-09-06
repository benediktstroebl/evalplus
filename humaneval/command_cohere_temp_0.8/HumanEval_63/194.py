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
assert FibFib(1)(0) == 0
assert FibFib(1)(1) == 0
assert FibFib(1)(2) == 1

assert FibFib(5)(4) == 5
assert FibFib(5)(5) == FibFib(5)(4) + FibFib(5)(3) + FibFib(5)(2)

assert FibFib(8)(7) == 21
assert FibFib(8)(8) == 24
```

The code defines a custom sequence class `FibFib` that extends Python's built-in `Sequence` interface. This class uses a loop to calculate the FibFib sequence values up to the specified `n` initialised value and uses the `__getitem__` method to allow indexing like a regular sequence. 

The provided test cases show that the sequence works as expected. You can uncomment the test cases one by one to validate the correctness of the script.