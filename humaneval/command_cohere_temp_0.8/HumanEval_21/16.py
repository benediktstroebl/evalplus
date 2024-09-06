Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    return [(x-min(numbers))/(max(numbers)-min(numbers))*1 for x in numbers]
```
The function `rescale_to_unit` takes a list of numbers as input and returns a transformed list where the smallest number is 0 and the largest number is 1. This is achieved by subtracting the minimum of the list and dividing by the difference between the maximum and the minimum of the list, and then multiplying by 1. 

This solution would produce a output:
```python
[0.0, 0.25, 0.5, 0.75, 1.0]
```

This approach assumes that the list of numbers has at least two elements.