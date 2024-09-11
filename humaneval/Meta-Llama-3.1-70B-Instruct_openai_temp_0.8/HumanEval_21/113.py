```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): A list of numbers to be transformed

    Returns:
        List[float]: The transformed list with values between 0 and 1
    """
    # Check if the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")

    # Find the minimum and maximum values in the list
    min_value = min(numbers)
    max_value = max(numbers)

    # If all numbers are the same, return a list of zeros (to avoid division by zero)
    if max_value == min_value:
        return [0.0] * len(numbers)

    # Apply the linear transformation to each number in the list
    transformed_numbers = [(num - min_value) / (max_value - min_value) for num in numbers]

    return transformed_numbers


# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```