```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    numbers = [0.1, 0.0, 0.0, 0.0, 0.5, 1.0]
    dry list = [numbers]
    numbers = [0.25 + x / 100 for x in numbers]
    print(numbers)
    assert 0 <= numbers[0] <= 1
    assert 0 <= numbers[1] <= 1
    assert 0 <= numbers[2] <= 1
    assert 0 <= numbers[3] <= 1
    assert numbers[0] + numbers[1] == 1
    assert numbers[2] + numbers[3] == 1
    assert numbers[0] * numbers[3] == numbers[0] * 4.0
   3
   0
   0])
```