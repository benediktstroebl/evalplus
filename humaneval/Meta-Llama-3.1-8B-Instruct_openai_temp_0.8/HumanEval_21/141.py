```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): List of float numbers

    Returns:
        List[float]: List of float numbers rescaled to the unit interval

    Raises:
        ValueError: If the input list has less than two elements
    """
    # Check if the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("The input list must have at least two elements")

    # Find the minimum and maximum numbers in the list
    min_val = min(numbers)
    max_val = max(numbers)

    # Check if the minimum and maximum values are the same
    if min_val == max_val:
        # If the list contains a single unique value, return a list of the same value
        return [0.0] * len(numbers)

    # Apply the linear transform
    rescaled_numbers = [(num - min_val) / (max_val - min_val) for num in numbers]

    return rescaled_numbers

# Test the function
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```
This script defines the `rescale_to_unit` function, which takes a list of float numbers and returns a new list with the numbers rescaled to the unit interval. The function first checks if the input list has at least two elements. If the list has less than two elements, it raises a `ValueError`. Otherwise, it finds the minimum and maximum numbers in the list and applies the linear transform to rescale the numbers. Finally, it returns the rescaled list. The script also includes a test case to demonstrate the function's behavior.