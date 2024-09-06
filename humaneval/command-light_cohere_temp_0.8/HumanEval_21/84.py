Here's a self-contained Python script that solves the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    # Apply the linear transform
    numbers_rescale = [x / (x + 1.0) for x in numbers]
    return numbers_rescale
```
The function rescale_to_unit takes a list of numbers as input and returns a list of the same numbers after applying the linear transformation. The linear transformation is defined by the formula y = x / (x + 1.0). This formula ensures that the smallest number becomes 0 and the largest number becomes 1.