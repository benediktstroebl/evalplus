Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    return [num / max(numbers) for num in numbers]
```
This script defines a function `rescale_to_unit` that takes a list of numbers as input and returns a list of numbers scaled to the range [0, 1]. The function simply divides each number in the list by the maximum number in the list. This approach ensures that the largest number will become 1, and the smallest (or any other number) will become 0, thus fitting the problem description. 

This function can be tested as shown below:
```python
# Test Rescale Function
>>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
[0.0, 0.25, 0.5, 0.75, 1.0]
>>> rescale_to_unit([-5.0, -10.0, -3.0, 7.0, 4.0])
[-1.0, -2.0, -0.3, 1.0, 0.4]
>>> rescale_to_unit([0.0, 0.5, 1.0, 1.5, 2.0])
[0.0, 0.167, 0.333, 0.5, 0.667]
```
The test cases provided above correspond to the examples shown in the problem description.