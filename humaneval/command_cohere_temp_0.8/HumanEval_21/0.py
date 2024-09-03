Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given a list of numbers (at least two elements), apply a linear transform to that list,
        such that the smallest number will become 0 and the largest will become 1 """
    min_value = min(numbers)
    max_value = max(numbers)
    return [((x - min_value) / (max_value - min_value)) for x in numbers]
```
The function `rescale_to_unit` works with lists of numbers, it first finds the minimum and maximum values in the list, and then divides each number in the list by the difference between the maximum and the minimum, thereby placing the minimum at 0 and the maximum at 1. 

Here's a simple test case to ensure that the function behaves as expected:
```python
test_rescale = [1.0, 2.0, 3.0, 4.0, 5.0]
expected_rescale = [0.0, 0.25, 0.5, 0.75, 1.0]
assert rescale_to_unit(test_rescale) == expected_rescale
```
If you want to test the function on other use-cases, you can uncomment the varying test cases and assert accordingly. 

This script provides a self-contained function that solves the problem as outlined in the prompt and also includes basic testing to ensure the function's behavior.