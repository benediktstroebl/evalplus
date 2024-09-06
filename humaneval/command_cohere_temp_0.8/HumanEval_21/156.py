Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    return [(x-min(numbers))/(max(numbers)-min(numbers))*1 for x in numbers]
```
The function `rescale_to_unit` takes a list of numbers as input and returns a transformed list such that the smallest number in the list becomes 0 and the largest number becomes 1. This is done by calculating the minimum and maximum values in the list, and then computing the linear transformation for each element. The computed transformation is applied to the original list, resulting in a new list where the elements are rescaled between 0 and 1. 
The script does not rely on any external variables or functions, making it self-contained and easy to use in different environments. 

Here is an example of using the `rescale_to_unit` function:
```python
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))
```
The output of this code is:
```
[0.0, 0.25, 0.5, 0.75, 1.0]
```
This demonstrates how the provided function can be used to rescale a list of numbers to the range [0, 1].