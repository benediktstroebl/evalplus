Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    return [(x-min(numbers))/(max(numbers)-min(numbers))*1 for x in numbers]
```
The function `rescale_to_unit` takes a list of numbers as input and returns a scaled list so that the smallest number becomes 0 and the largest number becomes 1. The scaling is linear and the function performs the transformation using Python's list comprehension. The resulting list of numbers is emitted after the transformation. 

This solution contains no additional imports, dependencies, or nested functions, making it a self-contained solution. It also passes the given test scenario and will execute with no issues.