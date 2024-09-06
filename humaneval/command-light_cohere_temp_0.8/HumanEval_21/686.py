```python
from typing import List
def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    # Conversion to type List[float] to ensure the function works with Python's floating-point numbers
    numbers = [num / 100.0 for num in numbers]
    return numbers
```
The provided Python function, named rescale_to_unit, takes a list of numbers as input and returns a new list with the same elements but potentially scaled up to the range [0, 1]. 

This function efficiently scales the input numbers by dividing each value by 100. The result is a same as it would be achieved using the map function and a linear transformation. 

The function has been designed to be efficient, with a time complexity of O(n), where n is the number of elements in the input list.