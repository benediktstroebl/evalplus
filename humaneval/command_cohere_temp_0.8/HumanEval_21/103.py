```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    # Find the minimum and maximum values in the list
    min_value = min(numbers)
    max_value = max(numbers)
    
    # Calculate the rescaled values
    rescaled = [(value - min_value) / (max_value - min_value) for value in numbers]
    
    return rescaled
```

The function `rescale_to_unit` takes a list of numbers as input and returns a list of rescaled values. It first identifies the minimum and maximum values within the input list using the `min` and `max` functions. Then, it applies a linear transformation to each value in the list, subtracting the calculated minimum value and dividing by the difference between the maximum and minimum values. This transformation ensures that the smallest number in the list becomes 0, and the largest number becomes 1.

Here's an example of using the function with a sample list of numbers:
```python
sample_numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
rescaled_numbers = rescale_to_unit(sample_numbers)
print(rescaled_numbers)
```

Output:
```
[0.0, 0.25, 0.5, 0.75, 1.0]
```

The function successfully transforms the input list, adjusting each value based on the extremes of the list.