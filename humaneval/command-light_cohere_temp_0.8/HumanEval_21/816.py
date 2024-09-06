```python
from typing import List


def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    Test: assert rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5]) == [([0.0, 0.0, 0.0, 0.0, 1])
   
Test: assert rescale_to_unit([1.0, 1.0]) == [([0.0, 0.0])
Test: assert rescale_to_unit([0.0, 0.0, 2]) == [ [1.0, 0.0])
Test: assert rescale_to_unit([0.0, 0.0, 0.0, 1.0]) == [([0.0, 0.0, 0])

print(rescale_to_unit([1.0, 2.0]))  #< 'Output: [0.5, 0.0]

print(rescale_to_unit([0.0, 0.0, 2]))  #< 'Output: [0.0, 0.0]')
print(rescale_to_unit([0.0, 0]))  #< 'Output: [1.0, 0]'
print(rescale_to_unit([0.0, 0.0]))  #< 'Output: [0.0, 0.0])