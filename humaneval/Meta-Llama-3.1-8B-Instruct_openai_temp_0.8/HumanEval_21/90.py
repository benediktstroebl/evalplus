### Rescale Numbers to Unit Interval
#### Problem Statement
Given a list of numbers, apply a linear transform such that the smallest number becomes 0 and the largest becomes 1.

#### Solution
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): A list of floating point numbers

    Returns:
        List[float]: The rescaled list of numbers

    Raises:
        ValueError: If the input list has less than two elements
    """
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")

    min_value = min(numbers)
    max_value = max(numbers)
    if min_value == max_value:
        return [0.0] * len(numbers)

    rescaled_numbers = [(num - min_value) / (max_value - min_value) for num in numbers]
    return rescaled_numbers

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
rescaled_numbers = rescale_to_unit(numbers)
print(rescaled_numbers)
```
In this script, we first check if the input list has at least two elements. If not, we raise a `ValueError`. We then find the minimum and maximum values in the list. If the minimum and maximum values are the same, we return a list of zeros, as the entire list can be mapped to a single point in the unit interval.

Finally, we apply a linear transformation to each number in the list. We subtract the minimum value from each number and divide by the range of the list (i.e., the maximum value minus the minimum value) to map the numbers to the unit interval. The result is a list of rescaled numbers.