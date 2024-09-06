Here's a self-contained Python function that solves the problem of finding the rolling maximum element in a list of integers:
```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    rolling_maxes: [int] = [num for num in numbers]
    max_num = numbers[0]
    
    for i in range(1, len(numbers)):
        max_num = max(rolling_maxes[i - 1], numbers[i])
        rolling_maxes[i] = max_num
        
    return rolling_maxes
```

This function takes a list of integers as input and uses a sliding window approach to efficiently calculate the list of rolling maximum elements. It initializes a a list to store the previous maximum values, and then iterates through the input list, updating the rolling maximum list with each element. The final result is a list of rolling maximum elements found in the input sequence.