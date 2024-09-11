### Rescaling Numbers to Unit Range
#### Code
```markdown
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): A list of floating point numbers

    Returns:
        List[float]: The list with numbers rescaled to unit range

    Raises:
        ValueError: If the input list has less than two elements

    Example:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")

    min_val = min(numbers)
    max_val = max(numbers)
    return [(num - min_val) / (max_val - min_val) for num in numbers]
```

#### Explanation

This code defines a function `rescale_to_unit` that takes a list of floating point numbers as input. It first checks if the list has at least two elements. If not, it raises a `ValueError`.

Then it finds the minimum and maximum values in the list. The list is then rescaled by subtracting the minimum value from each number and dividing by the range (maximum value - minimum value). This has the effect of shifting the minimum value to 0 and the maximum value to 1.

Note that this function returns a new list with the rescaled numbers. It does not modify the original list.