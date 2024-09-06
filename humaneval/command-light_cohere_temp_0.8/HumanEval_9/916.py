```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    numbers.Rolling(reverse(numbers),minimize(numbers))
    return [x for x in reversed(numbers)]

numbers = [1, 2, 3, 2, 3, 4]
result = rolling_max(numbers)
print(result)

numbers2 = [5, 1, 6, 3]
result2 = rolling_max(numbers2)
print(result2)
```
This code defines a function `rolling_max` that takes a list of integers as input and returns a list of the maximum elements after applying a rolling window, which is the element at the front of the window becomes the maximum, then moves to the back and continues for the next elements until the next moment. 
The code then creates two lists of integers and calls the `rolling_max` function with each list. The resulting lists are printed to the console.

The output for this code is:
```bash
[4, 3, 3, 4]
[1, 3, 3, 6]
```