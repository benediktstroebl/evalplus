Here is a self-contained Python script that solves the markdown code block problem:
```python
from typing import List


def rescale_to_unit(numbers: List[float]):
    numbers.extend(lambda x: (x - min(numbers)) / (max(numbers) - min(numbers)) if x < min(numbers) else (x - max(numbers)) / (min(numbers) - max(numbers)))
    return numbers
```
This function takes a list of numbers and applies a linear transform to that list, such that the smallest number will become 0 and the largest will become 1.  The function uses lambda functions to create a custom transformation that satisfies the problem constraints.