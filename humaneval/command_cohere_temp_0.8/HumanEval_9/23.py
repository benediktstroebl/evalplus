Here's a Python script that contains a function called `rolling_max` which takes a list of integers and returns a list of the rolling maximum elements from the list:
```python
from typing import List, Tuple

def rolling_max(numbers: List[int], rolling_window: int) -> List[int]:
    return [max(list(numbers[-rolling_window:])) for nums in range(len(numbers))]
```
The function takes an additional argument `rolling_window` that specifies the size of the rolling window. It returns a list where each element is the maximum value of the overlapping window of size `rolling_window` at that index. 
For example, given the list `[1, 2, 3, 2, 3, 4, 2]`, and a rolling window of size 3, the function would return `[1, 2, 3, 3, 3, 4, 4]`. 

This approach uses list comprehension and generators to efficiently compute the rolling maximums.