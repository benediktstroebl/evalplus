Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    numbers[:] = [x / max(numbers) for x in numbers]
    return numbers


# Test cases
numbers = [1.0, 2.0, 3.0, 4.0, 0, 0.0, 0.0, 0.0, 75]

rescale_to_unit(numbers)

# Test cases
numbers = [1.0, 2.0, 3.0, 4.0, 0, 0, 0]

rescale_to_unit(numbers)
```
The `rescale_to_unit` function is a self-contained function that takes a list of numbers and returns a new list with the numbers rescaled to the unit [0, 1]. The function works by dividing each number in the list by the largest number in the list, which ensures that the smallest number becomes 0 and the largest number becomes 1. 
This function is designed to solve the problem of scaling a list of numbers to the unit [0, 1] in a single, self-contained function.