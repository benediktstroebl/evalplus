```markdown
### Rescaling Numbers to Unit Range

This Python script defines a function `rescale_to_unit` that takes a list of numbers and applies a linear transformation to rescale the smallest number to 0 and the largest number to 1.
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): A list of numbers

    Returns:
        List[float]: The list of numbers rescaled to the unit range

    Example:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    # Check if the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("The list must have at least two elements")

    # Find the minimum and maximum numbers in the list
    min_num = min(numbers)
    max_num = max(numbers)

    # Check if the minimum and maximum numbers are the same
    if min_num == max_num:
        raise ValueError("The list must have different elements")

    # Apply the linear transformation
    rescaled_numbers = [(num - min_num) / (max_num - min_num) for num in numbers]

    return rescaled_numbers
```

### Example Usage:

```python
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
rescaled_numbers = rescale_to_unit(numbers)
print(rescaled_numbers)  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```
This script defines a function `rescale_to_unit` that takes a list of numbers, finds the minimum and maximum numbers, applies a linear transformation to rescale the smallest number to 0 and the largest number to 1, and returns the rescaled list. It also includes input validation and error handling to ensure that the list has at least two elements and different elements. The example usage demonstrates how to use the function with a sample list of numbers.