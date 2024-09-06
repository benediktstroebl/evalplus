Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    return [(x-min(numbers))/(max(numbers)-min(numbers)) * 1 for x in numbers]
```
The function `rescale_to_unit` takes a list of numbers as input and returns a scaled list so that the smallest number becomes 0 and the largest number becomes 1. You can test the function by calling it with a list of numbers and comparing the result to the expected output.  For example:
```python
>>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
[0.0, 0.25, 0.5, 0.75, 1.0]
```
This is the expected output for the input list provided in the original prompt.