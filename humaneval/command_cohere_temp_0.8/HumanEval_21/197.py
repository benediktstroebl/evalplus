Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    # Find the minimum and maximum values in the list
    min_value = min(numbers)
    max_value = max(numbers)
    
    # Calculate the rescaled values
    rescaled_numbers = [((x - min_value) / (max_value - min_value)) for x in numbers]
    
    return rescaled_numbers

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
rescaled = rescale_to_unit(numbers)
print(rescaled)
```

The function `rescale_to_unit` takes a list of numbers as input and returns a list of rescaled values. The `typing` module is used to indicate the input type. The code finds the minimum and maximum values in the input list using the `min` and `max` functions, respectively. Then, it calculates the rescaled values by subtracting the minimum value from each number, dividing by the difference between the maximum and minimum values, and returning the result. The `for` loop efficiently iterates through the list and computes the rescaled values. The printed output demonstrates the function's behavior, producing the expected result: `[0.0, 0.25, 0.5, 0.75, 1.0]`.