Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    return [num / max(numbers) for num in numbers]
```
This script defines a function `rescale_to_unit` that takes a list of numbers and normalizes it using a linear transformation. The function divides each number in the list by the maximum number in the list, ensuring the smallest number becomes 0 and the largest number becomes 1. 

Here is an example usage of the function:
```python
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
result = rescale_to_unit(numbers)
print(result)
```
The output will be:
```
[0.0, 0.25, 0.5, 0.75, 1.0]
```
This is the expected normalized result.