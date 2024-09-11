### Rescaling Numbers to a Unit Interval
#### Rescale to Unit Function
```python
from typing import List
import numpy as np

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.

    Args:
        numbers (List[float]): A list of floats (at least two elements) to rescale.

    Returns:
        List[float]: The rescaled list of numbers.

    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """

    # Ensure there are at least two numbers to compare
    if len(numbers) < 2:
        raise ValueError("List must contain at least two numbers")

    # Find the minimum and maximum values in the list
    min_value = np.min(numbers)
    max_value = np.max(numbers)

    # Apply the linear transformation
    rescaled_numbers = [(x - min_value) / (max_value - min_value) for x in numbers]

    return rescaled_numbers
```

### Example Usage
```python
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
rescaled = rescale_to_unit(numbers)
print(rescaled)  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```