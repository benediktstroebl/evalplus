Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    # Find the minimum and maximum values in the list
    min_value = min(numbers)
    max_value = max(numbers)
    
    # Calculate the rescaled values
    rescaled_numbers = [((x - min_value) / (max_value - min_value)) for x in numbers]
    
    # Return the rescaled list
    return rescaled_numbers

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
rescaled = rescale_to_unit(numbers)
print(rescaled)
```

The function `rescale_to_unit` takes a list of numbers as input and returns a list of rescaled values. The `rescaled_numbers` list computes the linear transformation, expressing each number in the list as a decimal fraction of the difference between the maximum and minimum numbers in the list.

The example usage demonstrates how to use the `rescale_to_unit` function to rescale the list `[1.0, 2.0, 3.0, 4.0, 5.0]` to `[0.0, 0.25, 0.5, 0.75, 1.0]`. 

This approach assumes that the list of numbers has at least two elements. Would you like to know more about the code?