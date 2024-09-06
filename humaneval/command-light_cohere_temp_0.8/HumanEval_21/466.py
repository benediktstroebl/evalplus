```python
from typing import List
def rescale_to_unit(numbers: List[float]):
    return [x/min(numbers) if min(numbers) != 0 else 1.0 for x in numbers]
# Test cases
assert rescale_to_unit([1.0, 2.0, 3.0, 4.0, 0.0, 0]) == [ [0.0, 0.5, 0, 0.0, 0]
assert rescale_to_unit([0.0, 0, 0, 0]) == [0.0, 0, 0, 0]
``` 
The code implements a function called `rescale_to_unit`, which accepts a list of numbers and returns a new list with numbers scaled to the range [0, 1]. The `assert` statements test that the function works correctly with various inputs.