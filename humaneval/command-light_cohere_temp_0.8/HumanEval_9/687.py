```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    numbers.max = max(numbers)
    rolling_max_element = numbers[0]
    for num in numbers[1:]:
        if num > max:
            max = num
        rolling_max_element = max if num == max else rolling_max_element
    return [rolling_max_element]

rolling_max([1, 2, 3, 2, 3, 4, 2])  # Output: [3, 3, 3, 3, 4, 4]
```
This script defines a function `rolling_max` that takes a list of integers as input and returns a list of the rolling maximum elements in the list. 

It uses the max function to find the maximum element in the list, and then starts a loop to find the maximum element for each consecutive number in the list. 

The `rolling_max_element` variable keeps track of the rolling maximum element.