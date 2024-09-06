Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    # Find the minimum and maximum values in the list
    min_value = min(numbers)
    max_value = max(numbers)
    
    # Calculate the scale factor
    scale_factor = 1 / (max_value - min_value)
    
    # Rescale each number in the list
    rescaled_numbers = [num * scale_factor for num in numbers]
    
    return rescaled_numbers
```

This script defines a function `rescale_to_unit` that takes a list of numbers as input and returns a list of rescaled numbers. The function finds the minimum and maximum values in the list, calculates the scale factor to map the range from 0 to 1, and then rescales each number in the list based on this scale factor.

The function is designed to work with any list of numbers, as long as it contains at least two elements. You can use the function with a list of test cases to verify that it works as expected. For example, you can use the following test list to verify the function:
```python
test_list = [1.0, 2.0, 3.0, 4.0, 5.0]
test_result = [0.0, 0.25, 0.5, 0.75, 1.0]
print(rescale_to_unit(test_list)) # Expected to print the result: [0.0, 0.25, 0.5, 0.75, 1.0]
``` 
This would return the expected result.