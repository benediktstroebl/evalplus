Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    # Find the minimum and maximum values in the list
    min_value = min(numbers)
    max_value = max(numbers)
    
    # Calculate the rescaled values
    rescaled_values = [((x - min_value) / (max_value - min_value)) for x in numbers]
    
    return rescaled_values
```

The function `rescale_to_unit` takes a list of numbers as input and returns a list of rescaled values between 0 and 1. It first finds the minimum and maximum values in the input list using the `min` and `max` functions. Then, it calculates the rescaled values by subtracting the minimum value from each number and dividing the result by the difference between the maximum and minimum values. This ensures that the smallest number in the list becomes 0, and the largest number becomes 1.

Here's an example usage of the function:
```python
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
rescaled = rescale_to_unit(numbers)
print(rescaled)
```

Output:
```
[0.0, 0.25, 0.5, 0.75, 1.0]
```

This indicates that the original values have been rescaled to a range of 0 to 1 based on the largest and smallest values in the list.