Here's a Python function that solves the problem:
```markdown
### Rescaling Numbers to Unit Range

#### Problem Description
Given a list of numbers, apply a linear transform to that list, such that the smallest number becomes 0 and the largest becomes 1.

#### Solution
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Rescales a list of numbers to the unit range [0, 1].

    Args:
        numbers (List[float]): A list of at least two numbers.

    Returns:
        List[float]: The rescaled list of numbers.

    Example:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    # Check if the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("List must have at least two elements")

    # Find the minimum and maximum values in the list
    min_val = min(numbers)
    max_val = max(numbers)

    # Apply the linear transform to the list
    rescaled = [(x - min_val) / (max_val - min_val) for x in numbers]

    return rescaled
```
#### Example Usage
```python
# Test the function
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))
# Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```
This function works by first finding the minimum and maximum values in the input list. It then applies a linear transform to each number in the list by subtracting the minimum value and dividing by the range of the values (i.e., `max_val - min_val`). This transforms the smallest number to 0 and the largest to 1, with linear interpolation in between.