Here is a self-contained Python function that solves the problem you described:
```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.

    numbers: [0.0, 2.0, 3.0, 4.0, 5]
   0, 1.0] to apply the0, out the range of values. 

This function takes a list of numbers as input and applies a linear transformation to the list, such that the smallest number will become 0 and the largest will become 1. The function then returns the list of numbers.

Let's break down the code:
- The function is defined with the `from typing import List` line to use the List type from Python's typing module.
- The `def rescale_to_unit(numbers: List[float])` line defines the function `rescale_to_unit`, which takes a list of numbers as input and returns a new list of numbers after applying the `rescale_to_unit` function.
- Inside function uses the list of numbers and applies a linear transformation to it. Then, the function returns the new list of numbers.
- This return the list of numbers.