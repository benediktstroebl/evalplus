Here is a self-contained Python script that solves the problem:
```python
from typing import List
def rescale_to_unit(numbers: List[float]):
    # Apply a linear transform to the numbers list, such that the smallest number will become 0 and the largest will become 1
    numbers = [x / 100.0 for x in numbers] + [100.0] * [max(numbers)] * [1.0 / min(numbers)]
    return numbers
```
This function, rescale_to_unit, takes a list of numbers as input and returns a new list of the same numbers after applying a linear transformation. The function works by first creating a new list of numbers by dividing each number in the input list by 100. Then, the function adds a value of 100.0 to the list of the new numbers and then takes the minimum value of the new numbers and divides it by the maximum value of the new numbers. The function then multiplies the minimum value of the new numbers by the reciprocal of the maximum value of the new numbers, which effectively scales the numbers down. 

This function effectively scales the numbers down to the range of 0 to 1.