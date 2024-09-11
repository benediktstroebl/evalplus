### Rescaling a List of Numbers to Unit Interval
#### Solution

```markdown
### Code
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): A list of floating point numbers

    Returns:
        List[float]: The rescaled list of numbers
    """
    if len(numbers) < 2:
        raise ValueError("List must have at least two elements")

    min_val = min(numbers)
    max_val = max(numbers)
    
    # Check for division by zero
    if max_val == min_val:
        raise ValueError("All numbers in the list are identical")

    return [(n - min_val) / (max_val - min_val) for n in numbers]

### Example Usage
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```

### Explanation
This script defines a function `rescale_to_unit` that takes a list of floating point numbers as input and returns a new list where the smallest number becomes 0 and the largest becomes 1. The rescaling is done using a linear transform. The function first checks if the input list has at least two elements, and if the minimum and maximum values are different. If not, it raises a `ValueError`. The rescaling is then performed using a list comprehension.