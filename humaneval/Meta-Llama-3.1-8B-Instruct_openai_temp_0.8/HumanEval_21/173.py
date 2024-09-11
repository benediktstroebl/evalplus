```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): A list of numbers

    Returns:
        List[float]: The rescaled list of numbers

    Raises:
        ValueError: If the list has less than two elements
    """
    if len(numbers) < 2:
        raise ValueError("List must have at least two elements")

    min_val = min(numbers)
    max_val = max(numbers)
    if min_val == max_val:
        return [0.0] * len(numbers)

    return [(num - min_val) / (max_val - min_val) for num in numbers]


# Example usage
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))
# Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```

This script defines a function `rescale_to_unit` that takes a list of numbers and returns a new list with the same numbers rescaled to the unit interval [0, 1]. The rescaling is done by subtracting the minimum value from each number and then dividing by the range of the numbers. If the list has less than two elements, a ValueError is raised.

The script also includes an example usage of the function with the provided test case.