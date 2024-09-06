Here's a solution:
```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    # Apply a linear transform to that list, such that the smallest number will become 0 and the largest will become 1
    numbers = [x / 100 for x in numbers]
    return numbers
```

The function takes a list of numbers as input and applies a linear transformation to the list, such that the smallest number in the list will become 0, and the largest number will become 1. The function then returns the resampled list.