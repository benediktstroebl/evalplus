### Rescaling Numbers to Unit Range

Here is a Python script that defines a function to rescale a list of numbers to the unit range (0 to 1).

```markdown
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): A list of floating point numbers

    Returns:
        List[float]: The rescaled list of numbers

    Example:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("List must contain at least two elements")

    min_value = min(numbers)
    max_value = max(numbers)
    return [(x - min_value) / (max_value - min_value) for x in numbers]

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
rescaled_numbers = rescale_to_unit(numbers)
print(rescaled_numbers)
```

### Output:
```
[0.0, 0.25, 0.5, 0.75, 1.0]
```

This script defines a function `rescale_to_unit` that takes a list of numbers as input. It first checks if the list contains at least two elements. If not, it raises a `ValueError`.

Then it finds the minimum and maximum values in the list. It uses these values to calculate the rescaled values for each number in the list, and returns the rescaled list.

The script includes an example usage of the `rescale_to_unit` function, which rescales the list `[1.0, 2.0, 3.0, 4.0, 5.0]` to the unit range and prints the result.