```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    numbers = [n / 100 for n in numbers]
    return [x if x <= 1 else 1 - x for x in numbers]
```
This code has a self-contained function that transforms a list of numbers into a unit scale. The function applies a rescaling by dividing each number by 100, which effectively maps the numbers to the range [0,1] while maintaining relative proportions. The function then returns a list of numbers, effectively applying the rescaling transformation.