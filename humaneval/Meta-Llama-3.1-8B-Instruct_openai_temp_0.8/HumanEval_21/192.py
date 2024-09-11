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

    # Check if the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("The list must have at least two elements")

    # Find the smallest and largest numbers in the list
    min_num = min(numbers)
    max_num = max(numbers)

    # Check if the smallest and largest numbers are the same
    if min_num == max_num:
        return [0.0] * len(numbers)

    # Apply the linear transform
    rescaled_numbers = [(num - min_num) / (max_num - min_num) for num in numbers]

    return rescaled_numbers

# Test the function
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))
```

This script defines a function `rescale_to_unit` that takes a list of numbers and applies a linear transform to rescale the numbers to the range [0, 1]. It first checks if the list has at least two elements, then finds the smallest and largest numbers in the list. If the smallest and largest numbers are the same, it returns a list of zeros. Finally, it applies the linear transform using a list comprehension and returns the rescaled list of numbers. The function is then tested with a sample list of numbers.