Here's a self-contained Python function that resizes a list of numbers in Markdown format to a scale where 0 is the smallest value and 1 is the largest:

```python
from typing import List
def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    numbers = [1.0, 2.0, 3.0, 4.0, 5]

    a transformation: t(x) = 1 + (-x) / max(x)

    return numbers * [1 + (-x) / max(numbers)]
```