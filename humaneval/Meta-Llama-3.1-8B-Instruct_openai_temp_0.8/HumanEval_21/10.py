### Rescaling a List of Numbers to Unit Interval
#### Problem Description

Given a list of numbers, apply a linear transform to that list, such that the smallest number will become 0 and the largest will become 1.

#### Solution
```markdown
### Code

```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Rescales the given list of numbers to the unit interval [0, 1].
    
    Args:
    numbers: A list of at least two float numbers.
    
    Returns:
    A list of rescaled float numbers in the unit interval [0, 1].
    
    Example:
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    # Find the minimum and maximum values in the list
    min_val = min(numbers)
    max_val = max(numbers)
    
    # Check if all values are equal
    if min_val == max_val:
        return [0.0] * len(numbers)
    
    # Apply the linear transformation
    rescaled = [(n - min_val) / (max_val - min_val) for n in numbers]
    
    return rescaled
```

#### Example Usage

```python
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```

#### Explanation

1.  Find the minimum and maximum values in the given list `numbers`.
2.  Check if all values are equal. If they are, return a list of zeros.
3.  Apply the linear transformation to each number in the list by subtracting the minimum value and dividing by the range (maximum value - minimum value).
4.  Return the list of rescaled numbers.