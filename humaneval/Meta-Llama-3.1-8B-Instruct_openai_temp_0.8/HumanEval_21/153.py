### Rescale Numbers to Unit Range
#### Python Script

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

    Example:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("List must contain at least two elements")

    min_num = min(numbers)
    max_num = max(numbers)
    if max_num == min_num:
        raise ValueError("All numbers must be different")

    return [(n - min_num) / (max_num - min_num) for n in numbers]

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
rescaled_numbers = rescale_to_unit(numbers)
print(rescaled_numbers)
```

### Explanation

The `rescale_to_unit` function takes a list of numbers as input and returns a new list where the smallest number is 0 and the largest number is 1. The function first checks if the input list contains at least two elements and all numbers are different. If these conditions are not met, the function raises a `ValueError`. Otherwise, it calculates the minimum and maximum numbers in the list and uses these values to rescale the list. The rescaled list is then returned.