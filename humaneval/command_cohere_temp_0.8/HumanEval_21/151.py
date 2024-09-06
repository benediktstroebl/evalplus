Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    return [((x - min(numbers)) / (max(numbers) - min(numbers))) for x in numbers]
```
The function `rescale_to_unit` takes a list of numbers `numbers` as input and returns a transformed list where the smallest number is 0 and the largest number is 1. The transformation is a linear scaling based on the difference between the maximum and minimum values in the input list. The function uses the `min` and `max` functions to find the smallest and largest numbers in the list, respectively, andlist comprehension to apply the scaling transformation to each element in the list.

To demonstrate the functionality of the `rescale_to_unit` function, we can use the following sample input list and expected output list:
```python
>>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
[0.0, 0.25, 0.5, 0.75, 1.0]
```
The output list is achieved by applying the linear transformation to the input list, thereby achieving the desired result. 

This approach ensures that the resulting list maintains the relative order of values, satisfies the condition that the smallest number becomes 0, and the largest number becomes 1.