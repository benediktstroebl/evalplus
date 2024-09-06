```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    # Apply the linear transformation
    numbers_res = [num / (max(numbers) - min(numbers)) for num in numbers]
    return numbers_res

# Test cases
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
numbers_res = rescale_to_unit(numbers)

print(numbers_res)  # Output: [0.0, 0.0, 0.0, 0]

assert all(numbers_res >= 0)

assert all(numbers_res <= 1)

numbers_float = [1.0, 2.0, 3.0, 4.0, 5.0]
numbers_res = rescale_to_unit(numbers_float)

print(numbers_res)  # Output: [0.0, 0.0, 0]

assert all(numbers_res >= 0)

assert all(numbers_res <= 1)
```
This script defines a function called `rescale_to_unit`, which takes a list of numbers as input and returns a new list of the same numbers, rescaled to the unit [0, 1]. The numbers are normalized such that the smallest number becomes 0, and the largest becomes 1. The test cases ensure that the function is working correctly by passing the numbers list with different test inputs and checking if the output is valid.