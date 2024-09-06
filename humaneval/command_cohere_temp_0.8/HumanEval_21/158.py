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

The function `rescale_to_unit` takes a list of numbers as input and returns a list of rescaled values based on the maximum and minimum values in the input list, complying with the problem statement. The example usage demonstrates how to use the function to rescale a list of numbers.