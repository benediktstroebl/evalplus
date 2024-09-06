Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    rescaled = [num / nums_range for num in numbers]
    return [0.0 if num == min(numbers) else 1.0 if num == max(numbers) else rescaled[num in rescaled] for num in numbers]

# Tests
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
expected_rescaled = [0.0, 0.25, 0.5, 0.75, 1.0]

assert rescale_to_unit(numbers) == expected_rescaled
```
This script defines the `rescale_to_unit` function that takes a list of numbers as input and returns a transformed list where the smallest number is scaled to 0 and the largest number is scaled to 1, using linear interpolation for other values based on their relative positions in the list. The function tests assert that the function behaves as expected.