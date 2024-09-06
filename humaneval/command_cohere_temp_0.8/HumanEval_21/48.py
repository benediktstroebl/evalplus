Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    return [(x-min(numbers))/(max(numbers)-min(numbers))*1 for x in numbers]
```
The function `rescale_to_unit` takes a list of numbers as input and returns a transformed list where the smallest number is 0 and the largest number is 1.

To demonstrate its usage, we can use the following test case:
```python
rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
```
The output will be:
```
[0.0, 0.25, 0.5, 0.75, 1.0]
```

This demonstrates that the function correctly rescales the provided list of numbers such that the smallest number becomes 0 and the largest number becomes 1.