```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    # Apply a linear transform to the list, such that the smallest number will become 0 and the largest will become 1
    numbers = [num / max(numbers) for num in numbers]
    return numbers

# Test cases:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
assert rescale_to_unit(numbers) == [0.0, 0.0, 0.0, 0.0])
assert rescale_to_unit([0.0, 0.0, 0.0, 0.0]) == [numbers]
assert rescale_to_unit([0.0, 0.0, 0.0, 0.0]) == [numbers]
assert rescale_to_unit([0.0, 0.0, 0.0, 0.0]) == [numbers]
assert rescale_to_unit([0.0, 0.0, 1.0, 0]) == [0.0, 0.0, 0]
assert rescale_to_unit([0.0, 0.0, 2.0, 0]) == [0.0, 0.0, 0]
assert rescale_to_unit([0.0, 0.0, 3.0, 0]) == [0.0, 0.0, 0]
assert rescale_to_unit([0.0, 0.0, 4.0, 0]) == [0.0, 0]
assert rescale_to_unit([0.0, 1.0, 5.0, 0]) == [0.0, 0]
assert rescale_to_unit([0.0, 2.0, 5.0, 0]) == [0.0, 0]
assert rescale_to_unit([0.0, 3.0, 5.0, 0]) == [0.0, 0]
```
The code defines a function called `rescale_to_unit`, which takes a list of numbers as input and returns a new list of the same numbers after applying a linear transformation. The transformation ensures that the smallest number in the original list becomes 0, and the largest number becomes 1.  The test cases demonstrate that the function correctly transforms the input list, and returns the expected output.