```python
from collections import Sequence

class FibFib(Sequence):
    def __init__(self, n):
        self.n = n
        self.seq = [0, 0, 1]
        for i in range(3, n + 1):
            self.seq.append(self.seq[i - 1] + self.seq[i - 2] + self.seq[i - 3])

    def __getitem__(self, index):
        if index < 0 or index >= self.n:
            raise IndexError("Invalid index")
        return self.seq[index]

# Test cases
if __name__ == "__main__":
    print(FibFib(1)[1])
    print(FibFib(5)[5])
    print(FibFib(8)[8])
```

This code defines a custom sequence class `FibFib` that implements the desired FibFib sequence calculation. This class follows the chainable sequence definition and allows for indexing to retrieve elements. The provided test cases demonstrate the behaviour of the class and ensure its correctness. Let's break down the code step by step:
1. **Class Definition**:
   ```python
   class FibFib(Sequence):
   ```
   This code defines a class named `FibFib` that inherits from the built-in `Sequence` class. This inheritance allows the `FibFib` class to behave like a sequence, supporting indexing to retrieve elements.
2. **Constructor and Sequence Initialization**:
   ```python
   def __init__(self, n):
       self.n = n
       self.seq = [0, 0, 1]
       for i in range(3, n + 1):
           self.seq.append(self.seq[i - 1] + self.seq[i - 2] + self.seq[i - 3])
   ```
   The `__init__` method is the constructor for the `FibFib` class. It takes an integer `n` as a parameter, which indicates the size of the FibFib sequence to create. Initially, the `self.seq` attribute is initialized with the first three values of the sequence (0, 0, 1). Then, a loop iterates from 3 to `n + 1` (inclusive) to populate the `self.seq` attribute with the calculated FibFib values. Each value is computed as the sum of the three previous values, defined by the recursive relationship `fibfib(n) = fibfib(n-1) + fibfib(n-2) + fibfib(n-3)`.
3. **Indexing Handler**:
   ```python
   def __getitem__(self, index):
       if index < 0 or index >= self.n:
           raise IndexError("Invalid index")
       return self.seq[index]
   ```
   The `__getitem__` method is responsible for handling indexing on the `FibFib` object. It takes an `index` as a parameter and returns the corresponding element from the `self.seq` sequence. It includes a check to ensure that the index is valid, within the range of the constructed sequence. If the index is invalid, an `IndexError` is raised to prevent accessing out-of-range elements.
4. **Test Cases**:
   ```python
   if __name__ == "__main__":
       print(FibFib(1)[1])
       print(FibFib(5)[5])
       print(FibFib(8)[8])
   ```
   If the script is run directly (not imported as a module), it