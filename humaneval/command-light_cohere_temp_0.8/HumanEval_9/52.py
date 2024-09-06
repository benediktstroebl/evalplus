```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [x for x, n in zip(numbers, numbers) if n < x or numbers.][-1]
max(numbers)
```
We start by creating a function named `rolling_max`, which takes a list of integers as input and returns a new list with the maximum element found in the rolling window. 

The algorithm used here is a simple and efficient one, which is to compare the current number with the maximum found so far and then to select the larger one. 

The main logic of the function is to create a temporary list `numbers_over_window` by unzipping the `numbers` list using the `range` function, and then to iterate over this list and select the maximum element using the `max` function. 
This process repeats until the window reaches the end of the `numbers` list.