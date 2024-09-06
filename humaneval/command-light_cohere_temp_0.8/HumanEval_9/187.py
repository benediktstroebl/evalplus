```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    numbers.append(numbers[-1])  # Append last element to maintain order
    max_num = max(numbers)
    rolling_maxes = [max_num]
    
    for i in range(1, len(numbers)):
        current = numbers[i]
        if current > max_num:
            max_num = current
        rolling_maxes.append(max_num)
    
    return rolling_maxes

# Example usage:
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)
```
This code defines a function `rolling_max` that takes a list of integers as an argument and returns a new list of the maximum elements after applying a rolling window to the input list. 
The rolling window moves by one element each time, and it keeps track of the maximum element found in that window.