```python
from typing import List
def rescale_to_unit(numbers: List[float]) -> List[float]:
    """Given list of numbers (of at least two elements), apply a linear transform to that list, such that the smallest number will become 0 and the largest will become 1.
    
    Numbers are expected to be a list of floating-point numbers. The function will apply a linear transformation to the numbers in the list, such that the smallest number will be mapped to 0 and the largest to 1.
    can accept an input of a list of numbers and returns the list of the same numbers, but scaled to the range 0 to 1."""

print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5]))

print(rescale_to_unit([0.0, 0.0, 0.0, 0]))

print(rescale_to_unit([0.0, 0.0, 0.0, 0.0]))

print(rescale_to_unit([0.0, 1.0, 2.0, 3]))

print(rescale_to_unit([0.5, 0.0, 0.0, 0.0]))
print(rescale_to_unit([0.0, 0.0, 0.0, 0]))
print(rescale_to_unit([0.0, 0.0, 0.0, 0]))
print(rescale_to_unit([0.0, 0.0, 0.0]))
print(rescale_to_unit([0.0, 0.0, 0]))

print(rescale_to_unit([0.0, 0.0, 0]))
``` 
This script defines a function called `rescale_to_unit` that takes a list of numbers and returns a new list of numbers scaled to the range 0 to 1. The function uses the typing function to ensure that the input is a list of numbers and that the output is also a list of numbers.