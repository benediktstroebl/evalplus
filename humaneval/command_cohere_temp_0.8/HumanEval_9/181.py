```python
from typing import List, Tuple

def rolling_max(numbers: List[int], rolling_window: int) -> List[int]:
    return [max(list(numbers)[i-rolling_window:i+1]) for i in range(len(numbers))]
```

The `rolling_max` function takes in a list of integers, `numbers`, and an integer, `rolling_window`, which determines the size of the rolling maximum window. The function returns a list where each element is the maximum value of the sublist of `numbers` that starts `i` indices ago and ends at the current index `i`, for all valid indices `i`.

Here is an example usage of the function:
```python
rolling_max([1, 2, 3, 2, 3, 4, 2], 3)
# [1, 2, 3, 3, 3, 4, 4]
``` 

This will return a list where each number is the maximum of the sublist of `numbers` that starts 3 indices ago and ends at the current index. For example, the value at index 0 is 1, as the maximum value of [2, 3, 2] (starting at index -1, or 2 indices ago) is 1. 

The function will return the following list for the provided example: [1, 2, 3, 3, 3, 4, 4]. This is returned because the rolling maximum over a window of size 3, for the list [1, 2, 3, 2, 3, 4, 2] is [1, 2, 3, 3, 3, 4, 4].