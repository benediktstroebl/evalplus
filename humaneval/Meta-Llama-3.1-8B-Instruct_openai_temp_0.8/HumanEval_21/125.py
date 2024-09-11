```python
from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): A list of at least two float numbers

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

    # Check if the smallest number is equal to the largest number
    if min_num == max_num:
        # If they are equal, return a list of zeros (except for the first element which is 1)
        return [1.0] + [0.0] * (len(numbers) - 1)

    # Apply the linear transform
    rescaled_numbers = [(num - min_num) / (max_num - min_num) for num in numbers]

    return rescaled_numbers


# Test the function
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))
print(rescale_to_unit([5.0, 5.0, 5.0]))
print(rescale_to_unit([-1.0, -2.0, -3.0]))
```