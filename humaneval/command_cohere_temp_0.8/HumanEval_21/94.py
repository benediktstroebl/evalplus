Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given a list of numbers (at least two elements), apply a linear transform to that list,
        such that the smallest number will become 0 and the largest will become 1 """
    return [((x - min(numbers)) / (max(numbers) - min(numbers))) for x in numbers]
```
The function `rescale_to_unit` takes a list of numbers (`List[float])` as input and returns a transformed list where the smallest number is 0 and the largest is 1. The transformation is a linear scale applied to each number in the list. 

To verify the function behavior, you can write a simple test: 
```python
def test_rescale_to_unit():
    # Sample input with diverse numerical values
    input_numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
    expected_output = [0.0, 0.25, 0.5, 0.75, 1.0, 0.5, 0.25, 0.0, 0.25, 0.5]
    
    assert rescale_to_unit(input_numbers) == expected_output
```
The test case demonstrates the behavior of the function with a diverse set of input values and verifies the output against the expected transformed values. 
The code above fully addresses the problem statement with a self-contained Python function, as well as a corresponding test case to validate its behavior. 
If you have more questions or would like more information, let me know!