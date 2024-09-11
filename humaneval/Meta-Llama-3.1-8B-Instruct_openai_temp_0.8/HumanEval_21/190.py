Here is the Python script that meets the requirements:
```markdown
### Rescaling Numbers to Unit Range

The following Python script defines a function `rescale_to_unit` that rescales a list of numbers to a unit range, where the smallest number becomes 0 and the largest number becomes 1.

```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers: A list of float numbers

    Returns:
        A list of float numbers in the unit range [0, 1]

    Example:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("List must contain at least two elements")

    min_value = min(numbers)
    max_value = max(numbers)
    if max_value == min_value:
        raise ValueError("All numbers in the list are equal")

    return [(num - min_value) / (max_value - min_value) for num in numbers]

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
rescaled_numbers = rescale_to_unit(numbers)
print(rescaled_numbers)
```

This script defines the `rescale_to_unit` function, which first checks if the input list contains at least two elements and if all numbers in the list are equal. If either condition is not met, it raises a ValueError.

The function then calculates the minimum and maximum values in the list. If all numbers are equal, it raises a ValueError.

Finally, the function applies a linear transform to the input list, scaling each number to the range [0, 1] using the formula (num - min_value) / (max_value - min_value). The result is returned as a new list.

The script also includes an example usage of the `rescale_to_unit` function, which prints the rescaled numbers to the console.