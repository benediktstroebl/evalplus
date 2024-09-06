Here's a Python script that contains a function called `rolling_max` which takes a list of integers `numbers` as input and returns a list of rolling maximum elements found at any given moment in the sequence:
```python
from typing import List, Tuple

def rolling_max(numbers: List[int]) -> List[int]:
    max_so_far = float('-inf')
    result = []

    for num in numbers:
        if num > max_so_far:
            max_so_far = num
        result.append(max_so_far)

    return result

""" Example usage
>>> rolling_max([1, 2, 3, 2, 3, 4, 2])
[1, 2, 3, 3, 3, 4, 4]
"""
```

This script defines the `rolling_max` function, which uses a `max_so_far` variable to keep track of the maximum element encountered thus far. The function iterates through the input list, comparing each element to the `max_so_far`, and updates it whenever a larger element is encountered. The maximum value at each step is appended to the `result` list, creating a list of rolling maximum elements. 

The example usage at the end demonstrates how the `rolling_max` function can be invoked with a predefined list.