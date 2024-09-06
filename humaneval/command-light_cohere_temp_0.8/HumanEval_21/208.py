Here's the self-contained Python function that solves the problem:
```python
from typing import List
def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    numbers = [1.0, 2.0, 3.0, 4.0, 5]
   
    [0.0, 0.0, 0.0])
   (numbers)
    numbers = [x / 100.0 for x in numbers]
    numbers = [100.0 * y + 100.0 * x / 100.0 for y in numbers]
    numbers = [min(numbers)] + [max(numbers)] * 1.0 / 100.0
    are numbers)
    numbers = [100.0 * x / min(numbers) + 100.0 * x / max(numbers) for x in numbers]
    return numbers
``` 
This function will help you to create a markdown code block that contains the rescale_to_unit function.