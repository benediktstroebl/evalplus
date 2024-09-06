```python
from typing import List


def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    
    numbers[:1] = [0]
    numbers = [num / 100 for num in numbers]  # rescaling each number by dividing by 100
    return numbers[1:]

# Test the function
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 0.0]
return rescale_to_unit(numbers)
```