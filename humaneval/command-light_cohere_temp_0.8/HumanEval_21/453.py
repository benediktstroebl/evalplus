Here's the Python code that you can use to solve the problem:
```python
from typing import List
def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.

    Input: numbers (list of floats)
    Output: List of floats, transformed such that 0 is the smallest number and 1 is the largest number in the list.

Test Case:
 numbers = [1.0, 2.0, 3.0, 4.0, 5.0]

result = rescale_to_unit(numbers)
print(result)
```
This function transforms a list of numbers so that it will have the same order as the input list, but the smallest number becomes 0 and the largest number becomes 1.