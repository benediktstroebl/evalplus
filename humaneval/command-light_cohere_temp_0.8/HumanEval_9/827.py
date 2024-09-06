```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    max_rolls = 0
    max_element = numbers[0]
    current_max = numbers[0]
    
    for num in numbers[1:]:
        current_max = max(num, current_max)
        max_rolls += 1
    
    return [current_max for _ in range(max_rolls)]

# Test case 1
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)
```

This script defines a function `rolling_max` that calculates and returns a list of rolling maximum elements from a given list of integers. The function uses a initial value of the first element in the list, then iterates through the remaining elements and keeps track of the current maximum element and the number of rolls to find the maximum element. 

It utilizes the `max()` function to update the current maximum element and counts the number of rolls.