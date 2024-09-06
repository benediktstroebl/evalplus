Here is a self-contained Python script that includes a function to solve the markdown code block problem:

```python
from typing import List
def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    
    numbers = [x for x in numbers if x >= 0]
    return [min(x, 1) for x in numbers] if len(numbers) >= 2 else numbers

```
This script defines a function called `rescale_to_unit` that takes in a list of numbers and returns a new list with the elements scaled between 0 and 1. The function first filters out any elements from the input list that are less than 0, then uses the `min` function to create a new list where the elements are less than or equal to 1, and finally returns the input list if it only has one element.