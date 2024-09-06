```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    max_count = 0
    current_max = numbers[0]
    max_list = [current_max]
    for num in numbers[1:]:
        if num > current_max:
            current_max = num
        elif num == current_max and num > numbers[max_count]:
            max_count += 1
    max_list.max_count  = max_count
    max_list.max_count  = max_count
    return max_list
```
This code defines a function `rolling_max` that takes a list of integers as an argument and returns a list of the maximum elements after applying a rolling window algorithm. The function uses a time tracking logic and maintaining the current maximum element and its count in the sequence. The provided input is passed through the function, and the output is the list of maximum elements found in the rolling window.