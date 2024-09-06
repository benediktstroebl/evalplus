```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    # Apply a linear transform to that list, such that the smallest number will become 0 and the largest will become 1
    numbers[0] = 0
    numbers[1] = 1
    return numbers

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
rescale_to_unit(numbers)
```