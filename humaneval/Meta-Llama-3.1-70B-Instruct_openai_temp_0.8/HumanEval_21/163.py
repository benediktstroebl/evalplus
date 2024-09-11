```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given a list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.

    Args:
        numbers (List[float]): A list of floating point numbers.

    Returns:
        List[float]: The input list after applying the linear transformation.
    """
    
    # Check if the list has less than two elements
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")

    # Find the minimum and maximum values in the list
    min_value = min(numbers)
    max_value = max(numbers)
    
    # If all numbers are the same, return a list of zeros (to avoid division by zero)
    if min_value == max_value:
        return [0.0] * len(numbers)
    
    # Calculate the range of the numbers
    range_value = max_value - min_value
    
    # Apply the linear transformation to each number in the list
    return [(num - min_value) / range_value for num in numbers]


# Test the function
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
print(rescale_to_unit([5.0, 10.0, 15.0, 20.0, 25.0]))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
print(rescale_to_unit([10.0, 10.0, 10.0, 10.0, 10.0]))  # Output: [0.0, 0.0, 0.0, 0.0, 0.0]
```