```python
from collections import Sequence

class FibFib(Sequence):
    def __init__(self, n):
        self.n = n
        self.sequence = [0, 0, 1]
        for i in range(3, n + 1):
            self.sequence.append(self.sequence[i - 1] + self.sequence[i - 2] + self.sequence[i - 3])

    def __getitem__(self, index):
        if index >= self.n:
            raise IndexError("Invalid index")
        return self.sequence[index]

# Test cases
print(FibFib(1)[1])
print(FibFib(5)[5])
print(FibFib(8)[8])
```

This script defines a custom sequence class `FibFib` that implements the formula for the `FibFib` sequence. The `__getitem__` method is overridden to allow indexing access to elements of the sequence. Test cases are included to verify the behavior against the problem statement. The sequence behaves like a list, so you can access elements using indexing [n], where n is the position of the element you want to access. 

The solution is efficient because it only performs a constant amount of work per iteration, and thus linearly over the index. This means that computing the n-th FibFib number only takes constant time.