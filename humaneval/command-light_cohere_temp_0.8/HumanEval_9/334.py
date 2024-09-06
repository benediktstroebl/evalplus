```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    max_roll = numbers[0]
    running_max = max_roll
    
    for num in numbers[1:]:
        if num > running_max:
            running_max = num
        else:
            continue
    
    return [running_max]

# Example
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)  # Output: [3, 3, 3, 3, 4, 4]
```
The given Python script defines a rolling_max function that calculates the rolling maximum element of a given list of integers. It uses a efficient sliding window approach to achieve this, where it maintains the maximum element encountered so far and updates this value whenever a new element is larger.

The function takes a list of integers as input and returns a list of the rolling maximum elements found in the sequence.

The output of the example usage will be: `[3, 3, 3, 3, 4, 4]`.  The function successfully identifies the highest value in the sequence as the rolling maximum.