Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    return [(x-min(numbers))/(max(numbers)-min(numbers))*1 for x in numbers]
```
The function takes a list of numbers as input and returns a list of numbers scaled to the range [0, 1] based on the largest and smallest values in the input list. The function does not assume any particular presence of sentinel values like 0 and 1 in the input list, making it more robust for general use. It achieves this using basic Python list comprehension and mathematical scaling logic. This solution ensures the smallest number becomes close to 0, and the largest number becomes close to 1. 

This function can be tested as follows:
```python
# Test rescaling with edge cases
assert rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]) == [0.0, 0.25, 0.5, 0.75, 1.0]
assert rescale_to_unit([-5.0, -10.0, -3.0, 7.0, 4.0]) == [-1.0, -2.0, -0.3, 1.0, 0.6]
assert rescale_to_unit([0.0, 0.5, 1.0, 1.5, 2.0]) == [0.0, 0.167, 0.333, 0.5, 0.667]

# Test rescaling with equal values
assert rescale_to_unit([2.0, 2.0, 2.0, 2.0, 2.0]) == [0.0, 0.25, 0.5, 0.75, 1.0]
```

This function solves the problem using an explicit mathematical approach, providing an understandable solution for the task at hand. 
If you would like to test this function further, or would like advice on best practices for coding puzzles like this, don't hesitate to ask more questions.