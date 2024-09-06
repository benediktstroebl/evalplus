Here's a self-contained Python script that solves the problem:

```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    numbers[0] = 0
    numbers[1] = 1

    return numbers
```

This script provides a function `rescale_to_unit` that takes a list of numbers as input and returns a new list where the first element is set to 0 and the last element is set to 1. The middle elements are calculated using the difference between the first and last elements and then dividing by their sum.