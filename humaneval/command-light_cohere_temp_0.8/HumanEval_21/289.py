Here is a self-contained Python script that solves the problem:

```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    
    numbers = [numbers[0] / numbers[1:] + numbers[0]]
    for x in numbers[1:]:
        x = x - numbers[0] / numbers[1]
    return [x + numbers[0] for x in numbers]
```
The function takes a list of numbers as input and applies a linear transform to the list. The linear transform is such such such mathematical operation such that scales the numbers to the range [0, 1] such that the minimum number becomes 0 and the maximum becomes 1. 

The function then returns a new list that contains the transformed numbers.