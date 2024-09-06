Here is a Python script that contains a self-contained function that solves the problem:
```python
from typing import List


def rescale_to_unit(numbers: List[float]):
    # Apply a linear transform to that list, such that the smallest number will become 0 and the largest will become 1
    numbers[0] = 0
    for n in numbers: n = (n - numbers[0]) / (numbers[-1] - numbers[0])
    return numbers
```
This function takes a list of numbers as input and applies a linear transformation to that list, such that the smallest number will become 0 and the largest will become 1. 

The function uses the "type" suggestion to create a function that takes a list of floats as input.

To test this function, you can create a sample list of numbers, pass it to the function, and then verify that the output is correct.