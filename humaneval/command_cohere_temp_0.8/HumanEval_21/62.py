Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    rescaled = [((x - min(numbers)) / (max(numbers) - min(numbers)) * 1) for x in numbers]
    return rescaled
```
The function `rescale_to_unit` takes a list of numbers as input and returns a list of numbers scaled to the range [0, 1]. The transformation is a linear transformation that maps the smallest number to 0 and the largest number to 1. 

You can verify the function's behavior by calling it on the example input provided in the problem statement:
```python
>>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
[0.0, 0.25, 0.5, 0.75, 1.0]
```
This output is as expected.