```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    
    # Validation tests
    assert len(numbers) == 2
    assert all(type(num) == float for num in numbers)
    assert numbers[0] + numbers[1] == 1.0
   0
   0, 0, 0, 0, 0, 0, 0, 0, 0, 0] = numbers
    assert numbers[0] * numbers[1] == 1.0
   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] != numbers
    assert numbers[0] >= 0 and numbers[1] >= 0
    assert min(numbers) == 0
    assert max(numbers) == 1
    assert numbers[0] + numbers[1] == 1.0
   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    return [x / 1.0 for x in numbers]
```