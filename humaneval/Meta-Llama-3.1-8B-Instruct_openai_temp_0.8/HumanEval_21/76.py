### Rescaling a List of Numbers to Unit Range

Below is a Python function that takes a list of numbers and returns a new list where the smallest number is 0 and the largest is 1. This is a common operation in data processing and machine learning.

```markdown
### `rescale_to_unit` Function
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    
    Args:
    numbers (List[float]): A list of floating point numbers.
    
    Returns:
    List[float]: A new list with numbers rescaled to the unit range.
    
    Example:
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """

    # Check if the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("List must have at least two elements")

    # Find the smallest and largest numbers in the list
    min_num = min(numbers)
    max_num = max(numbers)

    # Check for division by zero
    if min_num == max_num:
        raise ValueError("All numbers in the list are the same")

    # Apply the linear transform
    rescaled_numbers = [(num - min_num) / (max_num - min_num) for num in numbers]

    return rescaled_numbers
```

### Example Usage
```python
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
rescaled_numbers = rescale_to_unit(numbers)
print(rescaled_numbers)  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```