```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers: A list of floating point numbers

    Returns:
        A list of floating point numbers where the smallest number in the input list is mapped to 0
        and the largest number is mapped to 1
    """
    # Check if the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("List must contain at least two elements")

    # Find the minimum and maximum values in the list
    min_val = min(numbers)
    max_val = max(numbers)

    # Check if all values in the list are equal
    if min_val == max_val:
        return [0.0] * len(numbers)

    # Apply the linear transform
    rescaled = [(x - min_val) / (max_val - min_val) for x in numbers]

    return rescaled


# Example usage
if __name__ == "__main__":
    numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
    print(rescale_to_unit(numbers))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```

This script defines a function `rescale_to_unit` that takes a list of floating point numbers and returns a new list where the smallest number is mapped to 0 and the largest number is mapped to 1. The function first checks if the input list has at least two elements. If not, it raises a ValueError. It then finds the minimum and maximum values in the list, and applies a linear transform to each number in the list. If all values in the list are equal, it returns a list of zeros. The example usage at the end of the script demonstrates how to use the function with a list of numbers.