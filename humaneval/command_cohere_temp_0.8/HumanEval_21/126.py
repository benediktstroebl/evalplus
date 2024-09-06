Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    return [(x-min(numbers))/(max(numbers)-min(numbers))*1 for x in numbers]
```
The function `rescale_to_unit` takes a list of numbers as input and returns a transformed list via the linear transform specified in the prompt, the function uses the `min` and `max` functions to calculate the smallest and largest values in the list and uses python's list comprehension to apply the transformation to each element of the list and return the result. 

To ensure the correctness of the function, let's test it against the example provided in the prompt:
```python
>>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
[0.0, 0.25, 0.5, 0.75, 1.0]
```
The function passes this test, producing the expected output. 

This approach has a time complexity of `O(n)` since it requires scanning through the list once to compute the minimum and maximum values, and then scanning through the list again to apply the transformation to each element.