```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Applies a linear transform to the input list of numbers, 
    such that the smallest number becomes 0 and the largest number becomes 1.

    Args:
        numbers (List[float]): A list of numbers (at least two elements).

    Returns:
        List[float]: The rescaled list of numbers.
    """
    # Check if the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")

    # Find the minimum and maximum values in the list
    min_value = min(numbers)
    max_value = max(numbers)

    # Check if all numbers are the same
    if min_value == max_value:
        return [1.0] * len(numbers)

    # Calculate the range of the values
    value_range = max_value - min_value

    # Apply the linear transform to each number in the list
    rescaled_numbers = [(num - min_value) / value_range for num in numbers]

    return rescaled_numbers


# Test the function
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))  # [0.0, 0.25, 0.5, 0.75, 1.0]
print(rescale_to_unit([10.0, 20.0, 30.0, 40.0, 50.0]))  # [0.0, 0.25, 0.5, 0.75, 1.0]
print(rescale_to_unit([5.0, 5.0, 5.0, 5.0, 5.0]))  # [1.0, 1.0, 1.0, 1.0, 1.0]
```