Here's a self-contained Python function that generates a list of rolling max elements found until a given moment in the sequence:
```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    max_element = numbers[0]
    rolling_max_list = [max_element]
    for num in numbers[1:]:
        current_max = max(max_element, num)
        rolling_max_list.append(current_max)
        max_element = current_max
    return rolling_max_list
```

This code defines a function called rolling_max, which takes a list of integers as an argument and generates a new list that contains the rolling maximum elements found in the input list. It uses the old maximum element as the new maximum and updates the rolling_max list accordingly.