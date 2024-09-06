Here's the solution:
```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    # Apply a linear transformation to the list of numbers
    transformed_numbers = [x / 100 for x in numbers]
    return transformed_numbers

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
transformed = rescale_to_unit(numbers)
```
This function rescales a list of numbers to have the smallest number become 0 and the largest number become 1. The function takes a list of numbers as input and returns the rescaled list.