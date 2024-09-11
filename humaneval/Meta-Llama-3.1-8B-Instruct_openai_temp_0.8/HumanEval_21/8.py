```python
from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): A list of numbers to be rescaled

    Returns:
        List[float]: The rescaled list of numbers

    Example:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("The list must contain at least two elements")

    min_val = min(numbers)  # Find the smallest number
    max_val = max(numbers)  # Find the largest number

    if min_val == max_val:  # If all numbers are the same, return a list of zeros
        return [0.0] * len(numbers)

    # Calculate the rescaling factor
    rescale_factor = 1 / (max_val - min_val)

    # Apply the linear transform to each number
    rescaled_numbers = [(x - min_val) * rescale_factor for x in numbers]

    return rescaled_numbers


# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```

In this script, the `rescale_to_unit` function takes a list of numbers as input, calculates the smallest and largest number in the list, and then applies a linear transformation to each number to scale it to the range [0, 1]. The example usage at the end demonstrates how to use this function with a sample list of numbers.