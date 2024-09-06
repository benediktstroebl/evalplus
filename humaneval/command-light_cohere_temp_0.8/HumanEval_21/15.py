Here's the self-contained Python script that solves the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    numbers[:] = [x / 100.0 for x in numbers]
    return numbers
```
This script takes a list of numbers as an argument, and applies a linear transformation to that list, such that the smallest number will become 0 and the largest will become 1. It does this operation using the`numbers[:]` to apply the operation to the elements in the list.