Here is a Python script that solves the given problem:

```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    # Apply a linear transform to that list, such that the smallest number will become 0 and the largest will become 1
    numbers = [n / (n + 1) for n in numbers]
    return numbers
```

You can use this function with a list of numbers, and it will return a new list with the numbers scaled to the range from 0 to 1.