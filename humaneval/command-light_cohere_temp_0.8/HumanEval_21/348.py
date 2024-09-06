```python
from typing import List
def rescale_to_unit(numbers: List[float]):
    return [x / min(numbers) for x in numbers] if numbers else numbers[0] < min(numbers) else numbers]
```
This function takes a list of numbers and returns a new list where each element is the rescaled value to the range [0,1] such that the smallest value in the original list becomes 0 and the largest value becomes 1. 

To test the function, you can create a sample list of numbers and pass it to the function.