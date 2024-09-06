Here's the answer to your problem:
```python
from typing import List
def rescale_to_unit(numbers: List[float]) -> List[float]:
    # Apply a linear transform to the list, such that the smallest number will become 0 and the largest will become 1
    numbers = [x / 100.0 for x in numbers]
    return numbers
```
The above function takes a list of numbers as input and returns a new list where each number has been rescaled to the range [0,1].  This can be useful for any scenario where we want to transform a list of numbers in such a way.