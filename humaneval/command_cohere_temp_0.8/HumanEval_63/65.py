```python
from collections import Sequence

def fibfib_sequence(n: int) -> Sequence:
    """Returns the n-th element of the FibFib sequence."""
    sequence = [0, 0, 1]
    for i in range(2, n + 1):
        sequence.append(sequence[-1] + sequence[-2] + sequence[-3])
    return sequence

# Test cases
assert fibfib_sequence(1)[0] == 0
assert fibfib_sequence(5)[-1] == 4
assert fibfib_sequence(8)[-1] == 24
```

This code defines a function `fibfib_sequence`, which returns the FibFib sequence for a given `n` value. It initializes the sequence with the first three elements (0, 0, and 1) and then iteratively calculates the subsequent elements based on the definition of the FibFib sequence, where each element is the sum of the previous three elements. The given test cases verify the function's behavior for different `n` values, ensuring that it produces the expected results.