Here is a Python script that contains a self-contained function to solve the problem and pass the test:
```python
from typing import List


def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    
    numbers = [n / (n + 1) for n in numbers]
    return numbers

# Test the function with a set of numbers
test_numbers = [0.2,0.0,5, 0.05, 0.0, 5.0, 0.0, 2, 0.0, 1.0]

rescale_to_unit(test_numbers)

# The output should be a list of numbers in the range [0, 1]
```
This code defines a function called `rescale_to_unit` that takes in a list of numbers, and returns a new list where each number has been rescaled to the range [0, 1]. The test_numbers list is then passed into the function, and the function returns the resulting list. This list contains the0 numbers in the unit [0, 1].