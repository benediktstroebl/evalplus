Here is a self-contained Python function that solves the problem of applying a linear transformation to a list of numbers so that the smallest number becomes 0 and the largest becomes 1:
```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    # Ensure there are at least two elements in the list
    if len(numbers) < 2:
        raise ValueError("Input list must contain at least two elements")

    # Apply the linear transformation
    numbers[0] = min(numbers[0], 0)
    numbers[1] = max(numbers[1], 1)

    return numbers
```