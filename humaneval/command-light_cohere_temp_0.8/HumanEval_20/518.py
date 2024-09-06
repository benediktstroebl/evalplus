Here is the Python script that solves the problem:

```python
from typing import List

def find_closest_elements(numbers: List[float]):
    # Select the closest elements
    a, b = min(numbers[0], numbers[1]), max(numbers[0], numbers[1])
    return a, b
```

You can use this function by passing in the list of numbers that you want to find the closest pair from.