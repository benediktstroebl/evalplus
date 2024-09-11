```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Applies a linear transformation to the given list of numbers, 
    such that the smallest number becomes 0 and the largest becomes 1.

    Args:
    numbers (List[float]): A list of at least two floating point numbers.

    Returns:
    List[float]: The transformed list of numbers.
    """
    # Check if the list contains at least two elements
    if len(numbers) < 2:
        raise ValueError("The input list must contain at least two elements.")

    # Find the minimum and maximum values in the list
    min_value = min(numbers)
    max_value = max(numbers)

    # If all numbers are the same, return a list of zeros with the last element as 1
    if min_value == max_value:
        return [0.0] * (len(numbers) - 1) + [1.0]

    # Apply the linear transformation to each number in the list
    transformed_numbers = [(num - min_value) / (max_value - min_value) for num in numbers]

    return transformed_numbers


# Example usage
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```