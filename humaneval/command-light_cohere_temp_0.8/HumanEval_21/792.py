Here is a self-contained Python script that solves the markdown code block problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
   0)  numbers.apply(lambda x: x <= 0)
numbers = [x for x in numbers if x <= 0]
return numbers
```