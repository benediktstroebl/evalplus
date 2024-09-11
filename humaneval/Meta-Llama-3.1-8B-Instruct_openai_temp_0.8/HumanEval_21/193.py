Here's a self-contained Python script that solves the problem:

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
        raise ValueError("The input list must contain at least two elements")

    min_num = min(numbers)
    max_num = max(numbers)

    if max_num == min_num:
        # all elements are the same, rescale to [0.0, 0.0,...]
        return [0.0] * len(numbers)

    return [(n - min_num) / (max_num - min_num) for n in numbers]


# Test the function
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))
print(rescale_to_unit([10.0, 10.0, 10.0, 10.0, 10.0]))
print(rescale_to_unit([5.0, 5.0, 5.0, 5.0, 5.0, 5.0]))
```

This script does the following:

*   Checks if the input list has at least two elements. If not, it raises a `ValueError`.
*   Finds the minimum and maximum values in the list.
*   If all elements are the same, it returns a list with all elements set to 0.0.
*   Otherwise, it applies the linear transform to each element in the list using a list comprehension.
*   Finally, it prints the results for three test cases.