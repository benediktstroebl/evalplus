```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): A list of at least two float numbers.

    Returns:
        List[float]: The rescaled list of numbers.

    Examples:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    # Check if the input list has at least two elements
    if len(numbers) < 2:
        raise ValueError("The input list must have at least two elements")

    # Find the minimum and maximum values in the list
    min_val = min(numbers)
    max_val = max(numbers)

    # Check if all numbers are equal (i.e., min_val == max_val)
    if min_val == max_val:
        # If all numbers are equal, return a list of zeros
        return [0.0] * len(numbers)

    # Apply a linear transform to the list
    rescaled = [(num - min_val) / (max_val - min_val) for num in numbers]

    return rescaled

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
rescaled_numbers = rescale_to_unit(numbers)
print(rescaled_numbers)
```

In this script, we first check if the input list has at least two elements. If not, we raise a `ValueError`. Then, we find the minimum and maximum values in the list. If all numbers are equal, we return a list of zeros. Otherwise, we apply a linear transform to the list by subtracting the minimum value from each number and then dividing by the range of the list (i.e., the difference between the maximum and minimum values). The result is a list of numbers between 0 and 1, where the smallest original number becomes 0 and the largest becomes 1.