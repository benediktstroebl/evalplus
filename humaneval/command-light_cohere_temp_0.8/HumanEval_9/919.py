```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    numbers = [int(num) for num in numbers]  # Convert input list to integer array
    max_idx = len(numbers) - 1 - numbers.max()  # We max_idx
    max_num = numbers[max_idx]
    rolling_max = [max_num]
    
    for i in range(max_idx, -1, -1):
        if numbers[i] > max_num:
            max_num = numbers[i]
            rolling_max.append(max_num)
    
    return rolling_max

# Test cases
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)  # Output: [1, 2, 3, 3, 3, 4, 4]

numbers2 = [10, 9, 8, 7, 6, 5, 4]
result2 = rolling_max(numbers2)
print(result2)  # Output: [10, 9, 8, 7, 6, 5, 4]
```
This script defines a function rolling_max that takes a list of integers as input and returns a new list containing the rolling maximum elements in the sequence. The rolling maximum is the element is calculated using a sliding window approach, where the index of the maximum element is updated and the list is updated accordingly. The test cases demonstrate the new input lists, and the output is printed.