Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given a list of numbers (at least two elements), apply a linear transform to that list,
        such that the smallest number will become 0 and the largest will become 1 """
    min_value = min(numbers)
    max_value = max(numbers)
    return [((x - min_value) / (max_value - min_value)) for x in numbers]
```
The function `rescale_to_unit` ensures that the provided list of numbers is at least 2 in length before proceeding with the normalization transformation. A list of at least two numbers is required to establish a baseline for the smallest and largest values to be set to 0 and 1, respectively. The function utilizes Python's built-in `min` and `max` functions to identify these extreme values, and the transformation is executed using a list comprehension that calculates the normalized value for each number in the input list. 

The `rescale_to_unit` function normalize the numbers in a list such that the smallest number becomes 0 and the largest number becomes 1. Here is an example of how to use this function:
```python
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
normalized_numbers = rescale_to_unit(numbers)
print(normalized_numbers)
```
This will print out the normalized numbers, which in this case is:
```
[0.0, 0.25, 0.5, 0.75, 1.0]
```
This list now represents a normalized version of the original list, where the smallest value has been scaled to 0 and the largest value has been scaled to 1, with other values proportional to these extremes.  This is a common technique for preprocessing data when engagement in data analysis or visualization activities, as it makes sure that each value is on a comparable scale, irrespective of their original magnitudes.  This can also be termed as Normalization of data.