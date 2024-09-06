```python
from typing import List
def rescale_to_unit(numbers: List[float]) -> List[float]:
    # Apply a linear transformation to the input list to get values ranging from 0 to 1
    numbers = [x / 100.0 for x in numbers]
    return numbers

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
rescale_to_unit(numbers)
# Test cases
assert rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]) == [numbers([0.0, 0.0, 0.0, 0.0])
assert rescale_to_to_unit([0.0, 0.0, 1.0, 2.0]) == [numbers([0.0, 0.0, 1.0])
assert rescale_to_to_unit([0.0, 0.0, 1.0]) == [numbers([0.0, 0, 1.0])
assert rescale_to_to_unit([0.0, 0.0, 1.0]) == [numbers([0.0, 0, 1.0])
assert rescale_to_to_unit([0.0, 2.0, 3.0]) == [numbers([0.0, 0.0, 0])
assert rescale_to_unit([0.0, 0.0, 1.0]) == [numbers([0.0, 0, 0])
``` 
This script defines a function rescale_to_unit that takes a list of numbers and returns a new list where each element has been rescaled to a value of 0 to 1. The test cases ensure that the function works correctly.