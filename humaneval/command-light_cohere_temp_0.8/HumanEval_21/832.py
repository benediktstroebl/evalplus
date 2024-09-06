Here is a Python script that includes a self-contained function that solves the problem of scaling down a list of numbers so that the smallest value becomes 0 and the largest value becomes 1:

```python
from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    numbers = [n / 100.0 for n in numbers]
    return [min(numbers) * 100.0 for n in numbers]
```

This function takes a list of numbers as input and returns a list of the same numbers, but each has been scaled to be between 0 and 1. This is a same way used to format a list of numbers in a way that makes it easier to read and understand.

It then applies a linear transformation to that list, such that the smallest number will become 0 and the largest will become 1.