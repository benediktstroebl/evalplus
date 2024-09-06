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

The function `rescale_to_unit` takes a list of numbers as input and returns a list of rescaled values between 0 and 1. The code first finds the minimum and maximum values in the input list using the `min` and `max` functions. It then calculates the rescaled values by subtracting the minimum value from each number, dividing by the difference between the maximum and minimum values, and then adding the minimum value back to ensure the values are within the range [0, 1].

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

This indicates that the original numbers have been rescaled to fit within the range [0, 1] while maintaining linear relationships between the original and rescaled values.