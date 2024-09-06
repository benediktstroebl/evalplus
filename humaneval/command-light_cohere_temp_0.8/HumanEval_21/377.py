```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    # Ensure the list has at least 2 elements
    if len(numbers) < 2:
        raise ValueError("Input list must contain at least two numbers")

    # Apply the transformation to each number
    new_numbers = [num / max(numbers) for num in numbers]

    return new_numbers
```
The function `rescale_to_unit` takes a list of numbers as input and applies a linear transformation to each number, such that the smallest number will become 0 and the largest will become 1. It uses the minimum and maximum values from the input list to calculate the rescaled values.

The function raises a `ValueError` if the input list does not have at least two elements, ensuring that the correct behavior is enforced.