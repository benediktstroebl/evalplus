Here's the solution to the problem:

```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    # Apply the rescaling transformation
    numbers_rescaled = [x / (x - min(numbers)) * 1.0 for x in numbers]
    # Return the transformed list
    return numbers_rescaled
```

This function takes a list of numbers as input and applies a linear transformation to that list, such that the smallest number will become 0 and the largest will become 1. It then returns the the necessary list of numbers.