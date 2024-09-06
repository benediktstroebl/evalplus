```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    :param numbers: List[float]
    :return: List[float]
    numbers = [num / 100 for num in numbers]
    return numbers

# Test cases
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 0.0]))
test_cases([1.0, 2.0, 3.0, 0, 0, 75])
```
This Python code defines a function called `rescale_to_unit` that performs a linear transformation on a list of numbers. It takes a input as a list of numbers and returns a new list where each element has been rescaled by dividing by 100. 

The test cases section demonstrates the function by passing different lists of numbers to it and printing the resulting rescaled values. 

This function is designed to scale the input list of numbers such that the smallest number becomes 0 and the largest becomes 1.