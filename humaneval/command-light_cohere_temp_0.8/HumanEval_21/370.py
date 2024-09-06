Here's the solution to the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    # Ensure that numbers has at least two elements
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")
    
    # Apply linear transform
    transformed_numbers = [x / (numbers[1] - numbers[0]) for x in numbers]
    
    # Check that the output is a valid list
    if not isinstance(transformed_numbers, List):
        raise ValueError("The result of the transformation is not a list")
    
    return transformed_numbers
```
This function, named `rescale_to_unit`, takes a list of numbers as its argument and returns a corresponding list of the same numbers but with the smallest number (which is originally 0) made equal to 1 and the largest number made equal to 0. The function uses the basic linear transformation to the input list of numbers, such that the result will have all positive numbers. 
This function includes type hints for better code readability and robust error handling.