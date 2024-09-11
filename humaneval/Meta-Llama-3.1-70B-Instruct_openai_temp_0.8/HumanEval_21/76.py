```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers: A list of numbers with at least two elements

    Returns:
        A new list where the smallest number is 0 and the largest number is 1
    """
    # Check if the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("The list must have at least two elements")

    # Find the minimum and maximum numbers in the list
    min_num = min(numbers)
    max_num = max(numbers)

    # If all numbers are the same, return a list of zeros with the same length
    if min_num == max_num:
        return [0.0] * len(numbers)

    # Calculate the scaling factor
    scaling_factor = 1 / (max_num - min_num)

    # Apply the linear transformation to the list
    rescaled_numbers = [(num - min_num) * scaling_factor for num in numbers]

    return rescaled_numbers

# Example usage:
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
print(rescale_to_unit([10.0, 20.0, 30.0, 40.0, 50.0]))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
print(rescale_to_unit([5.0, 5.0, 5.0, 5.0, 5.0]))  # Output: [0.0, 0.0, 0.0, 0.0, 0.0]
```