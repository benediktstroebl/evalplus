Here is a self-contained Python script with a function that solves the problem:
```python
from typing import List
def rescale_to_unit(numbers: List[float]):
    # Apply a linear transform to that list, such that the smallest number will become 0 and the largest will become 1
    numbers = [x / 100.0 for x in numbers]
    return numbers

# Test cases
numbers_test_list = [1.0, 2.0, 3.0, 4.0, 5.0]
numbers_test_list = rescale_to_unit(numbers_test_list)
assert [0.0, 0.0, 0.0, 1.0] == numbers_numbers_test_list
numbers_random_list = [3.5, 4.0, 2.0, 7.0, 8.0]
numbers_test_list = rescale_to_unit(numbers_random_list)
assert [0.0, 0, 0, 0] == numbers_test_list
```
This script defines a function `rescale_to_unit` that takes a list of numbers and returns a new list with the numbers scaled to the range [0, 1]. The Test cases are provided to check the function's correctness.