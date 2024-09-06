Here is a self-contained Python function that solves the problem:

```python
from typing import List


def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.

    # Make sure that the list of numbers is a list of at least 2 numbers
    numbers = [x for x in numbers if len(numbers) >= 2]

    # Apply a linear transform
    for i in range(len(numbers) - 1):
        numbers[i] = (numbers[i + 1] - numbers[i]) / (numbers[i + 1] - numbers[i])

    # Return the rescaled list
    return numbers
```

This function takes a list of numbers as input and applies a linear transformation to that list, such that the smallest number will become 0 and the largest will become 1. It then returns the
 list of the rescaled numbers.