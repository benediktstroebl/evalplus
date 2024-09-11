```markdown
### Rescaling Numbers to a Unit Interval

This Python script defines a function `rescale_to_unit` that applies a linear transform to a list of numbers.
The smallest number in the list will be rescaled to 0 and the largest will be rescaled to 1.

```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): A list of floating point numbers.

    Returns:
        List[float]: The rescaled list of numbers.

    Examples:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("At least two elements are required.")

    min_val = min(numbers)
    max_val = max(numbers)

    # Check for division by zero
    if max_val == min_val:
        raise ValueError("All numbers are the same.")

    rescaled = [(n - min_val) / (max_val - min_val) for n in numbers]
    return rescaled
```

### Example Usage

```python
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
rescaled_numbers = rescale_to_unit(numbers)
print(rescaled_numbers)  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```