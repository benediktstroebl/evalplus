```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    # Apply a linear transform to the input list to ensure that the smallest number is 0 and the largest is 1
    numbers = [x / 100.0 for x in numbers]
    return numbers

# Test case: pass corresponding tests
assert [1.0, 2.0, 3.0, 4.0, 5.0] == rescale_to_unit([1.0, 2.0, 3.0, 4.0, 0.0, 0.0, 0.5])

assert [1.0, 0] in numbers]
```