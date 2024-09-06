```python
from typing import List
def rescale_to_unit(numbers: List[float]) -> List[float]:
    # Ensure list has at least two elements
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")

    # Apply linear transform
    numbers = [num / min(numbers) for num in numbers]
    return numbers

# Example usage
input_numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print("Rescaled numbers:", rescale_to_unit(input_numbers))
```
This Python code defines a function called rescale_to_unit, designed to adjust a list of numbers so that it spans from 0 to 1. It operates by taking the minimum value in the list and dividing each number by this minimum to ensure they are all non-negative values and lie within the range [0,1] after scaling. The code handles input lists with at least two elements, raises a ValueError for lists with less than two elements, and returns a new list where each element has been rescaled.