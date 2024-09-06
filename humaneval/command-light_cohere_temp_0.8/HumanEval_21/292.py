```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    numbers = [0.0, 1.0, 2.0, 3.0, 4.0, 5]
   0, 0.5, 0]

numbers = (numbers / max(numbers)) if len(numbers)==1 else numbers = (numbers / max(numbers))

assert len(numbers) == 5
assert rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]) and assert (0.0) <= numbers < 0.0) and assert (0.0) <= numbers <= 1.0
assert rescale_to_unit([0.0, 1.0, 2.0, 3.0, 4]) is assert (0.0) <= numbers <= 0.0)
assert rescale_to_to_unit([0.0, 0.0, 0.0, 5]) is assert (0.0) <= numbers <= 0.0)
assert rescale_to_to_unit([0.0, 1.0, 2.0, 3]) is assert (0.0) <= numbers <= 1.0)
 assert rescale_to_unit([0.0, 0.0, 0.0, 1]) is assert (0.0) <= numbers <= 0.0)
 assert rescale_to_unit([0.0, 0.0, 0, 0.0]) is assert (0.0) <= numbers <= 1.0)
 rescale_to_unit([0.0, 0.0, 0, 1]) is assert (0.0) <= numbers <= 0.0)
 assert rescale_to_unit([0.0, 0.0, 2, 3]) is assert (0.0) <= numbers <= 1.0)
assert rescale_to_unit([0.0, 0.0, 0, 0]) is assert (0.0) <= numbers <= 0.0)
assert rescale_to_unit([0.0, 0.0, 0, 0, 4]) is assert (0.0) <= numbers <= 1.0)
 assert rescale_to_unit([0.0, 0.0, 0, 0]) is assert (0.0) <= numbers <= 0.0)
 print("Passed all tests")
```