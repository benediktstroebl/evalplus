```python
from collections import Sequence

def fibfib_seq(n: int):
    """Returns the n-th element of the FibFib sequence."""
    base_cases = [0, 0, 1]
    if n < 3:
        return base_cases[n]
    else:
        return fibfib_seq(n-1) + fibfib_seq(n-2) + fibfib_seq(n-3)

# Tests
print(fibfib_seq(1))
# Should print 0

print(fibfib_seq(5))
# Should print 4

print(fibfib_seq(8))
# Should print 24
```

This script defines a Python function `fibfib_seq` that calculates the n-th element of the FibFib sequence, as described in the problem statement. The function checks if `n` is less than 3; it returns the corresponding base case value (0 or 1). Otherwise, it recursively computes the n-th value by summing the previous three elements in the sequence.

The section titled "Tests" is a placeholder for test cases that you can implement to verify the correctness of the `fibfib_seq` function. In this context, it prints the results of calling `fibfib_seq` with certain input values and compares them to the expected outputs. You can add more tests to thoroughly validate the function's behavior for various `n` values.