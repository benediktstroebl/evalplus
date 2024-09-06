Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    return [(x-min(numbers))/(max(numbers)-min(numbers))*1 for x in numbers]
```
The function `rescale_to_unit` takes a list of numbers as input and returns a transformed list. The transformation applies a linear function to the input list, such that the smallest number in the list becomes 0 and the largest number becomes 1. This is achieved by subtracting the minimum and dividing by the difference between the maximum and the minimum. The resulting list contains numbers between 0 and 1, representing a linear scale of the original list. 
The script does not rely on any external libraries or modules for the transformation. Sample usage and output:
```python
# Sample usage
result = rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
print(result)  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]

``` 
This would output the expected scaled numbers, confirming the correct implementation of the transformation.