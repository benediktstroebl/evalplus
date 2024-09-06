Here is a self-contained Python script that solves the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    numbers[:] = [x / 100.0 for x in numbers]
    return numbers
```
This function is designed to transform a list of numbers into a unit of 0 to 1 range. It accomplishes this function by dividing each number in the list by 100, effectively scaling the numbers down to the range of 0 to 1. It is a self-contained function, which is why it does not require any additional inputs to work.