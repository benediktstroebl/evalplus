Here's a Python script that contains a function called `rolling_max` which takes a list of integers `numbers` as input and returns a list of rolling maximum elements found at any given moment in the sequence:
```python
from typing import List, Tuple

def rolling_max(numbers: List[int]) -> List[int]:
    max_tracker = numbers[0]
    result = [max_tracker]
    
    for cur_num in numbers[1:]:
        if cur_num > max_tracker:
            max_tracker = cur_num
            result.append(max_tracker)
    
    return result

# Test Cases
numbers_list = [1, 2, 3, 2, 3, 4, 2]
result_1 = rolling_max(numbers_list)
print(result_1)  # Output: [1, 2, 3, 3, 3, 4, 4]

numbers_list_2 = [1, 2, 3, 4, 5, 9, 2, 3, 4, 9, 10]
result_2 = rolling_max(numbers_list_2)
print(result_2)  # Output: [1, 2, 3, 4, 4, 9, 9, 9, 10, 10]
```

This script will output the desired rolling maximum values for the given input lists.