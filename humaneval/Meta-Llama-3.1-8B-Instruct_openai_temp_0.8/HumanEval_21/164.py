### Rescaling List of Numbers to Unit Range
#### Problem Description

Given a list of numbers, apply a linear transform to the list, such that the smallest number will become 0 and the largest will become 1.

#### Solution
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): List of numbers to be rescaled

    Returns:
        List[float]: Rescaled list of numbers
    """
    # Check if the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("List must have at least two elements")

    # Find the minimum and maximum numbers in the list
    min_num = min(numbers)
    max_num = max(numbers)

    # Check for division by zero
    if max_num == min_num:
        raise ValueError("All numbers in the list are equal")

    # Apply the linear transform
    rescaled_numbers = [(num - min_num) / (max_num - min_num) for num in numbers]

    return rescaled_numbers

# Example usage:
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))
# Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```
This script defines a function `rescale_to_unit` that takes a list of numbers and returns a new list with the same numbers rescaled to the unit range [0, 1]. The rescaling is done using a linear transform, where each number is mapped to a value between 0 and 1 based on its position relative to the minimum and maximum values in the list. The function includes error checking to ensure that the input list has at least two elements and that all numbers in the list are not equal.