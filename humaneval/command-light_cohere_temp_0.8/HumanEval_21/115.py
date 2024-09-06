Here is a Python script with a self-contained function that solves the problem:

```python
from typing import List


def rescale_to_unit(numbers: List[float]):
    # Apply a linear transform to that list,
    # such that the smallest number will become 0 and the largest will become 1
    numbers = [num / (max(numbers) - min(numbers)) + min(numbers) for num in numbers]
    return numbers
```

This function takes a list of numbers and applies a linear transformation to that list, such that the smallest number will become 0 and the largest will become 1. The function uses the interesting that it first finds the minimum and maximum values of the list, then it applies the transformation by dividing every number by the difference between the maximum and minimum, adding the minimum value.

The function then returns the resulting list of rescaled numbers.