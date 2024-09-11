```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): A list of at least two float numbers

    Returns:
        List[float]: The rescaled list of numbers
    """
    if len(numbers) < 2:
        raise ValueError("The list must contain at least two elements")

    # Find the minimum and maximum numbers in the list
    min_num = min(numbers)
    max_num = max(numbers)

    # Check if the minimum and maximum numbers are the same
    if min_num == max_num:
        raise ValueError("All numbers in the list are the same")

    # Calculate the scaling factor
    scale_factor = 1 / (max_num - min_num)

    # Apply the linear transform to the list
    scaled_list = [(num - min_num) * scale_factor for num in numbers]

    return scaled_list

# Example usage:
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))
# Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```

This Python script defines a function `rescale_to_unit` that takes a list of numbers and returns a new list with the same numbers but scaled to the range [0, 1]. The script also includes docstrings and example usage to demonstrate how the function works.