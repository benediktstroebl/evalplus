```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    """
    # Using list comprehension to make sure the list has at least 2 elements
    numbers = [x / 100.0 for x in numbers] + [100.0]
   0
   
     4.0]

def test_rescale_to_unit(numbers: List[float]):
    assert rescale_to_unit(numbers) == [0.0, 1.0, 3.0, 4.0]
assert len(numbers) == 2
    assert numbers == [1.0, 2.0, 3.0, 5.0]
assert numbers[numbers] == [0.0, 1.0, 3.0, 4.0]
   
assert numbers == [0.0, 0.0, 0.0, 0]
   assert numbers == [0.0, 0, 0, 0]
    assert numbers == [0.0, 0.0, 1.0, 1.0]
    assert numbers == [0.0, 0, 0.0, 1.0]
```