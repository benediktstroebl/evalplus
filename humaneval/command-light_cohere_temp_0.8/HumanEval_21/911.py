```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
   0

    transform numbers in that way.  The returned numbers will then be transformed to the unit of [-1,1] in the interval [0,1]
    new_numbers = [num / min(numbers) for num in numbers]
    return new_numbers

# Test cases
numbers = [1.0, 2.0, 3.0, 4.0, 5]
output: **[0.5, 0.0, 0.0, 0]**

numbers = [1.0, 2.0, 3.0, 4]
output: **[0.5, 0.0, 0.0, 0]**

numbers = [0.0, 0.0, 1.0, 2.0]
output: **[1.0, 0, 0.0, 0]**

numbers = [0.0, 0.0, 0.0, 0.0, 5]
output: **[0.0, 0.0, 0.0, 0]**

numbers = [0.0, 0.0, 0.0, 0.0, 6]
output: **[0.0, 0, 0.0, 0]**

numbers = [0.0, 0.0, 1.0, 3]
output: **[0.0, 0, 0.0, 0]**

numbers = [0.0, 0.0, 1.0, 3]
output: **[0.0, 0, 0.0, 0]**

numbers = [0.0, 0.0, 0.0, 1]
output: **[0.0, 0, 0].0**
```