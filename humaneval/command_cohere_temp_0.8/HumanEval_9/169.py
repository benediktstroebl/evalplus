Here's a Python script that contains a function called `rolling_max` that takes a list of integers `numbers` as input and returns a list of rolling maximum elements found in the sequence up to that point. The function is designed to work with lists that may contain duplicate elements and may have gaps in the sequence:
```python
from typing import List, Tuple

def rolling_max(numbers: List[int]) -> List[int]:
    rolling_max_vals = []
    max_tracker = numbers[0]
    
    for num in numbers[1:]:
        if num > max_tracker:
            max_tracker = num
        rolling_max_vals.append(max_tracker)
    
    return rolling_max_vals
```

The code uses a list `rolling_max_vals` to store the rolling maximum elements and tracks the maximum element found so far using the variable `max_tracker`. It then iterates through the list, updating `max_tracker` whenever a newer element is greater than the maximum element tracked. Ultimately this method is more efficient than calculating the rolling maximum every time, making it better for larger lists. And it's generally safer in cases where duplicates or gaps could confuse a list comprehension.