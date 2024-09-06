```python
from typing import List
def rescale_to_unit(numbers: List[float]):
    # Apply a linear transform to the list, such that the smallest number becomes 0 and the largest becomes 1
    new_numbers = [x / 100.0 for x in numbers]
    return new_numbers
```
Do you require additional assistance with any other Python-related or other topics?