```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): A list of floating point numbers

    Returns:
        List[float]: The input list, but with the smallest number becoming 0 and the largest becoming 1

    Raises:
        ValueError: If the list contains less than two elements

    Example:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("List must contain at least two elements")

    min_num = min(numbers)
    max_num = max(numbers)
    if min_num == max_num:  # Check for case when all numbers are the same
        return [0.0] * len(numbers)
    else:
        return [(num - min_num) / (max_num - min_num) for num in numbers]

# Example usage
if __name__ == "__main__":
    numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
    rescaled = rescale_to_unit(numbers)
    print(rescaled)  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```

This script defines the `rescale_to_unit` function, which takes a list of floating point numbers, rescales them to the range [0, 1], and returns the result. It also includes example usage and docstrings for clarity and documentation. The function raises a `ValueError` if the input list contains less than two elements.