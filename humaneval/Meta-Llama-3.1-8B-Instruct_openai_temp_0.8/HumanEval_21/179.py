```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): A list of at least two unique floating point numbers

    Returns:
        List[float]: The rescaled list of numbers

    Raises:
        ValueError: If the list contains duplicate numbers or less than two elements
    """
    # Check if the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("List must contain at least two elements")

    # Check if the list contains duplicate numbers
    if len(numbers)!= len(set(numbers)):
        raise ValueError("List must not contain duplicate numbers")

    # Find the minimum and maximum values in the list
    min_val = min(numbers)
    max_val = max(numbers)

    # Check if the minimum and maximum values are the same
    if min_val == max_val:
        raise ValueError("All numbers in the list must be unique")

    # Apply the linear transform
    rescaled = [(num - min_val) / (max_val - min_val) for num in numbers]

    return rescaled


# Example usage
if __name__ == "__main__":
    numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
    print(rescale_to_unit(numbers))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```

This script defines a function `rescale_to_unit` that takes a list of numbers and returns a new list where the smallest number has been transformed to 0 and the largest number has been transformed to 1. The function raises a `ValueError` if the list contains duplicate numbers or less than two elements. The example usage at the end shows how to use the function with a list of numbers.