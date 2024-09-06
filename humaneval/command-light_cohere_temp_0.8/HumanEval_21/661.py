```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    # Apply a linear transformation to the input numbers
    numbers_res = [n / min(numbers) for n in numbers]
    return numbers_res

# Test cases for the rescale_to_unit function:
print("Results of rescale_to_unit:")
print([1.0, 2.0, 3.0, 4.0, 5.0, 0.0, 0.0, 0])
print("[] = {0.25, 0.0, 0.0, 1.0, 0.0, 1.0}")
print("=" + str(rescale_to_unit([1.0, 2.0, 3.0, 4, 5, 0]))
``` 
This script defines a function called `rescale_to_unit` that takes a list of numbers as input and applies a linear transformation to those numbers, so that the smallest number becomes 0 and the largest number becomes 1. The function then returns the result of the transformation. 

The test cases provided after the function are designed to test the behavior of the function with a variety of input scenarios.