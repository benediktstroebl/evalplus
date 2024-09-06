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

The function `rescale_to_unit` takes a list of numbers as input and returns a list of rescaled values. The `rescale_to_unit` function works as follows:
1. To determine the minimum and maximum values in the input list, it uses the `min` and `max` functions. The range of the values in the list is thus determined.
2. It creates a new list called `rescaled_numbers` using a list comprehension. Each element in this list is obtained by dividing the difference between the value and the list's minimum value by the difference between the maximum and minimum values for each number in the input list. The values in the list are therefore linearly transformed.
3. The function finally returns the `rescaled_numbers` list, which contains the rescaled values. 

When you run the example, the output is:
```yaml
[0.0, 0.25, 0.5, 0.75, 1.0]
```

The numbers in this example have been rescaled so that the smallest value is 0 and the largest value is 1, corresponding to the requirement for this problem.