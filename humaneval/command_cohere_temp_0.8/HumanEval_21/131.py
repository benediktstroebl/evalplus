Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    return [((x - min(numbers)) / (max(numbers) - min(numbers))) for x in numbers]
```
The function `rescale_to_unit` takes a list of numbers as input and returns a list of numbers scaled to the range [0, 1] using the linear transformation described in the prompt. This transformation stretches the range of values in the list to cover the range [0, 1], with the smallest value in the list becoming 0 and the largest value becoming 1.

To help users understand the functionality, here is an example of using the function:
```python
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
result = rescale_to_unit(numbers)
print(result)
```
The output will be:
```
[0.0, 0.25, 0.5, 0.75, 1.0]
```
This transformation is useful in many data analysis and machine learning applications, where the network needs to interpret input values in the range of 0 to 1 to facilitate training and model optimization.