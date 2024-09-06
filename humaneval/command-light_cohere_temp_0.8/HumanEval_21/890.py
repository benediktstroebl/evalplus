```python
from typing import List
def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.
    """
    mathematical transformation that rescales a given list of numbers to the range [0,1]. The function takes a list of numbers and returns a new list with the same values but a rescaled scale. 

Test cases are passed to the function:
```python
numbers = [1.0, 2.0, 3.0, 4.0, 5]
numbers = [1.0, 2.0, 3.0, 4]
numbers = rescale_to_unit(numbers)
numbers = [1.0, 0.0, 0]
numbers = [0, 0, 0]
numbers = [0, 0, 0, 1]
numbers = [1, 0, 0, 1, 2]
numbers = [0, 0, 0, 1, 0, 3]
print(rescale_to_unit([1.0, 2.0, 3.0, 4])) # [Expected output: [0.0, 0.0, 0.0, 0.0]

numbers = [0.0, 0.0, 0]
numbers = [0.0, 0.0, 0.0]
numbers = rescale_to_unit(numbers)
print(rescale_to_unit([1.0, 2.0, 3.0, 4])) # [Expected output: [0.0, 0.0, 0.0, 1.0]
numbers = rescale_to_unit(numbers)
print(rescale_to_unit([0, 0, 0, 1])) # [Expected output: [0, 0, 0, 1]]
print(rescale_to_unit([0, 0, 0, 1], 2)) # [Expected output: [0, 0, 0, 2]]
```