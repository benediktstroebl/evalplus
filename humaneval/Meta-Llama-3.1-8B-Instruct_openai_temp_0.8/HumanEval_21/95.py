### Rescale Numbers to Unit Interval
#### Python Script

```python
from typing import List
import numpy as np

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): List of numbers to rescale

    Returns:
        List[float]: Rescaled list of numbers
    """

    # Check if the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("List should contain at least two elements")

    # Use NumPy's min and max functions to find the smallest and largest numbers
    min_val = np.min(numbers)
    max_val = np.max(numbers)

    # Check if all numbers are equal
    if min_val == max_val:
        return [0.0] * len(numbers)

    # Apply the linear transform
    rescaled_numbers = [(n - min_val) / (max_val - min_val) for n in numbers]

    return rescaled_numbers

### Example Usage
if __name__ == "__main__":
    numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
    print(rescale_to_unit(numbers))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```

This script uses a list comprehension to apply the linear transform to each number in the input list. It first finds the smallest and largest numbers using NumPy's min and max functions, and then scales each number by the same factor to ensure the smallest number becomes 0 and the largest becomes 1. If all numbers in the list are equal, it returns a list of zeros.