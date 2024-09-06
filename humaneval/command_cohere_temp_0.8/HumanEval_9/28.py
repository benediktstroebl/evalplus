Here is a Python script with a self-contained function that solves the problem:
```python
from typing import List, Tuple

def rolling_max(numbers: List[int], rolling_window: int) -> List[int]:
    return [max(list(numbers)[i-rolling_window:i+1]) for i in range(len(numbers))]
```

The function takes in a list of numbers and an integer `rolling_window` that indicates the size of the rolling window. The function returns a list of integers, where each integer in the list is the maximum value in the rolling window at that moment in the list. 

Here is an example call:
```python
rolling_max([1, 2, 3, 2, 3, 4, 2], 3)
```
Which would return:
```
[1, 2, 3, 3, 3, 4, 4]
```
This is because the rolling maximum of the list [1, 2, 3, 2, 3, 4, 2] with a window size of 3 at each moment is: [1, 2, 3, 3, 3, 4, 4]. 

This approach uses a list comprehension to find the maximum element in the rolling window at each position in the list. Let me know if this solves the problem!