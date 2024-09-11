```markdown
## Rescale Numbers to Unit Range
### Problem Description

Given a list of numbers, we need to apply a linear transform to that list, 
such that the smallest number becomes 0 and the largest becomes 1.

### Solution

```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): A list of float numbers

    Returns:
        List[float]: The rescaled list of numbers

    Example:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    # Check if the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("The list must have at least two elements")

    # Find the minimum and maximum numbers in the list
    min_num = min(numbers)
    max_num = max(numbers)

    # Check if the minimum and maximum numbers are the same
    if min_num == max_num:
        # If they are the same, return a list of zeros
        return [0.0] * len(numbers)

    # Apply the linear transform
    rescaled_list = [(num - min_num) / (max_num - min_num) for num in numbers]

    return rescaled_list

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```

### Explanation

1. First, we check if the list has at least two elements. If not, we raise a ValueError.
2. Then, we find the minimum and maximum numbers in the list.
3. If the minimum and maximum numbers are the same, we return a list of zeros.
4. Otherwise, we apply the linear transform by subtracting the minimum number and dividing by the range of the numbers.
5. Finally, we return the rescaled list of numbers.