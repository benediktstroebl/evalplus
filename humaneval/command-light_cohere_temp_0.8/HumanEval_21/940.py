Here is a self-contained Python function that solves the problem you described:
```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    # Ensure length of numbers list is at least 2
    if len(numbers) < 2:
        raise ValueError("Input list must contain at least two elements")
    
    # Apply linear transformation
    transformed_numbers = [num / (max(numbers) - min(numbers))] + [min(numbers)]
    return transformed_numbers
```
This function takes a list of numbers as input and returns a list of the same numbers but with the values scaled to be between 0 and 1. It also includes input validation to ensure that the input list contains at least two elements.