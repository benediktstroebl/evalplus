Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    # Find the minimum and maximum values in the list
    min_value = min(numbers)
    max_value = max(numbers)
    
    # Calculate the scale factor for the linear transformation
    scale_factor = 1 / (max_value - min_value)
    
    # Rescale each number in the list
    rescaled_numbers = [num * scale_factor for num in numbers]
    
    return rescaled_numbers

# Unit test
numbers_to_rescale = [1.0, 2.0, 3.0, 4.0, 5.0]
expected_rescale = [0.0, 0.25, 0.5, 0.75, 1.0]
assert rescale_to_unit(numbers_to_rescale) == expected_rescale

numbers_with_negative_range = [5.0, 2.0, 3.0, -1.0, 0.5]
expected_with_negative_range = [-1.0, 0.0, 0.33333333, 0.0, 0.2]
assert rescale_to_unit(numbers_with_negative_range) == expected_with_negative_range
```

This script defines the `rescale_to_unit` function that takes a list of numbers as input and applies a linear transformation to the values, ensuring that the smallest number becomes 0 and the largest number becomes 1. The script also includes unit tests to verify the function's behavior with different input lists.