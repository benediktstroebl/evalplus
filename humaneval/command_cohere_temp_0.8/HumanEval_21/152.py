Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    return [(x-min(numbers))/(max(numbers)-min(numbers))*1 for x in numbers]
```
The function `rescale_to_unit` takes a list of numbers as input and returns a transformed list such that the smallest number in the list becomes 0 and the largest number becomes 1. This is achieved by calculating the minimum and maximum values in the list, and applying a linear transformation to each element in the list. The test case provided in the prompt is also included here in the code:
```python
# Test the function
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
expected = [0.0, 0.25, 0.5, 0.75, 1.0]
print(rescale_to_unit(numbers) == expected)
```
The function should return `True` based on the provided test case. 
You can add more test cases to further validate the function's behavior.