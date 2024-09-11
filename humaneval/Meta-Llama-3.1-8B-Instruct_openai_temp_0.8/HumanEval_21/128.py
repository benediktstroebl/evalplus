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

    Examples:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    # Check if the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("List must have at least two elements")

    # Find the minimum and maximum numbers in the list
    min_num = min(numbers)
    max_num = max(numbers)

    # Check if all numbers in the list are equal to avoid division by zero
    if min_num == max_num:
        return [0.0] * len(numbers)

    # Apply the linear transform
    rescaled_numbers = [(num - min_num) / (max_num - min_num) for num in numbers]

    return rescaled_numbers

# Test the function
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))
```

This script defines a function `rescale_to_unit` that takes a list of numbers as input and returns a new list where the numbers have been rescaled to the range [0, 1]. The function first checks if the input list has at least two elements. If not, it raises a `ValueError`. It then finds the minimum and maximum numbers in the list and applies a linear transform to each number in the list. If all numbers in the list are equal, it returns a list of zeros to avoid division by zero. The function is then tested with the example provided.