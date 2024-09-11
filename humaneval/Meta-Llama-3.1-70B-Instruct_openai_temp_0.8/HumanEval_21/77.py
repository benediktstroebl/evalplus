```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Applies a linear transform to the input list, rescaling it to the unit range [0, 1].

    Args:
    numbers (List[float]): A list of numbers with at least two elements.

    Returns:
    List[float]: The input list rescaled to the unit range [0, 1].
    """

    # Check if the input list has at least two elements
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")

    # Find the minimum and maximum values in the list
    min_value = min(numbers)
    max_value = max(numbers)

    # Check if all numbers are the same to avoid division by zero
    if min_value == max_value:
        return [0.0] * len(numbers)

    # Apply the linear transform to rescale the list to the unit range [0, 1]
    rescaled_numbers = [(x - min_value) / (max_value - min_value) for x in numbers]

    return rescaled_numbers


# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
rescaled_numbers = rescale_to_unit(numbers)
print(rescaled_numbers)  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```