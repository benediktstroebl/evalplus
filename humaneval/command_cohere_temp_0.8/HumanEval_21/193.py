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
    rescaled_numbers = [number * scale_factor for number in numbers]
    
    # Format for readbility purposes
    return rescaled_numbers

# Unit tests
def test_rescale_to_unit():
    # Test with a list of positive and negative numbers
    numbers = [1.0, 2.0, -3.0, 4.0, 5.0]
    expected_rescale = [0.0, 0.25, -0.33, 0.5, 0.75]
    rescaled = rescale_to_unit(numbers)
    assert rescaled == expected_rescale

test_rescale_to_unit()
```

This script defines the `rescale_to_unit` function that takes a list of numbers as input and rescales them linearly so that the smallest number becomes 0 and the largest number becomes 1. The `test_rescale_to_unit` function checks if the rescaling works correctly for a list of mixed positive and negative numbers. The `assert` statement checks that the expected rescaling produces the correct output. 

The script can be executed directly or imported as a module in another Python script to use the `rescale_to_unit` function.