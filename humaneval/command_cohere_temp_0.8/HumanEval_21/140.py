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

The function `rescale_to_unit` ensures that the input list has at least two elements before attempting to calculate the range. It then calculates the minimum and maximum values in the list and computes the range using these values. Finally, it applies the linear transformation to the input list, which rescales the numbers such that the smallest number becomes 0 and the largest number becomes 1. This approach guarantees that the 'range' attribute is calculated correctly, providing robust behavior for input lists of different sizes. 

Here is a simple test case to ensure the function behaves correctly:
```python
test_list = [1.0, 2.0, 3.0, 4.0, 5.0]
test_result = [0.0, 0.25, 0.5, 0.75, 1.0]

assert rescale_to_unit(test_list) == test_result
``` 

And the output of this code will be:
```bash ...
``` 
Note that the function raises a `ValueError` exception if the input list has less than two elements, verifying that the function behaves correctly with incorrect input as well.