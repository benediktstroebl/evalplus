```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given a list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.
    """
    if len(numbers) < 2:
        raise ValueError("At least two numbers are required to compute the range.")
    min_value = min(numbers)
    max_value = max(numbers)
    return [((x - min_value) / (max_value - min_value)) for x in numbers]
```

The function `rescale_to_unit` ensures that the input list has at least two elements before proceeding with the transformation. It then calculates the minimum and maximum values in the list and computes the range of values. Finally, it applies a linear transformation to the numbers, scaling them between 0 and 1 based on the range. This approach guarantees that the smallest number in the list becomes 0, and the largest number becomes 1.

Here is an example of using this function:
```python
round_numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
result = rescale_to_unit(round_numbers)
print(result)
```

The output will be:
```
[0.0, 0.25, 0.5, 0.75, 1.0]
``` 

This indicates that the original numbers have been correctly scaled between 0 and 1. 
The code includes type hints and adheres to Python's type-checking feature, "Type Hinting", which improves code readability and maintainability. Furthermore, the function's behavior is clearly defined by the docstring, which provides quick information on the function's objectives and usage.