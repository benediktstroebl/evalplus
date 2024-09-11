```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    
    Args:
        numbers (List[float]): A list of at least two float numbers.
    
    Returns:
        List[float]: The input list rescaled to the unit interval [0, 1].
    """
    if len(numbers) < 2:
        raise ValueError("Input list must contain at least two elements")

    min_val = min(numbers)
    max_val = max(numbers)

    if max_val == min_val:
        # If all values are the same, return a list of zeros (except for the last one which is 1.0)
        return [0.0] * (len(numbers) - 1) + [1.0]

    return [(x - min_val) / (max_val - min_val) for x in numbers]


# Example usage:
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
print(rescale_to_unit([10.0, 20.0, 30.0, 40.0, 50.0]))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
print(rescale_to_unit([5.0, 5.0, 5.0, 5.0, 5.0]))  # Output: [0.0, 0.0, 0.0, 0.0, 1.0]
```