```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): A list of floating point numbers

    Returns:
        List[float]: The input list with values rescaled to the unit interval

    Raises:
        ValueError: If the input list has less than two elements
        ValueError: If all elements in the input list are equal

    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """

    # Check if the input list has at least two elements
    if len(numbers) < 2:
        raise ValueError("The input list must have at least two elements")

    # Check if all elements in the input list are equal
    if len(set(numbers)) == 1:
        raise ValueError("All elements in the input list must be distinct")

    # Find the minimum and maximum values in the list
    min_value = min(numbers)
    max_value = max(numbers)

    # Check if the minimum and maximum values are equal
    if min_value == max_value:
        raise ValueError("All elements in the input list must be distinct")

    # Apply the linear transform to the list
    return [(x - min_value) / (max_value - min_value) for x in numbers]

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
rescaled_numbers = rescale_to_unit(numbers)
print(rescaled_numbers)
```
This script defines a function `rescale_to_unit` that takes a list of floating point numbers and returns a new list with the same numbers rescaled to the unit interval [0, 1]. The function first checks if the input list has at least two elements and if all elements are distinct. If these conditions are not met, it raises a `ValueError`. Then, it finds the minimum and maximum values in the list and applies a linear transform to the list to rescale the values. The result is a new list with the same numbers rescaled to the unit interval. The script includes example usage of the function and prints the rescaled numbers.