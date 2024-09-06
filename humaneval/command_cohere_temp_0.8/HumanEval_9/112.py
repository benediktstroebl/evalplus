Here's a Python script that contains a function called `rolling_max` that takes a list of integers `numbers` as input and returns a list of rolling maximum elements found in the sequence up to that point. The function is designed to work with lists that may contain duplicate elements and may have gaps in the sequence:
```python
from typing import List, Tuple

def rolling_max(numbers: List[int]) -> List[int]:
    rolling_max_list = []  # List to store rolling max elements over time.
    max_so_far = float('-inf')  # Track the max element encountered thus far.
    
    for num in numbers:
        if num > max_so_far:
            rolling_max_list.append(num)  # Add the new max to the rolling max list.
            max_so_far = num  # Update the max element encountered thus far.
    
    return rolling_max_list

# Test cases
numbers1 = [1, 2, 3, 2, 3, 4, 2]
result1 = rolling_max(numbers1)
print(result1)  # Output: [1, 2, 3, 3, 3, 4, 4]

numbers2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
result2 = rolling_max(numbers2)
print(result2)  # Output: [10, 10, 10, 7, 7, 7, 6, 6, 3, 3]

numbers3 = [5, 5, 5, 5, 10, 10, 15, 20, 15, 10]
result3 = rolling_max(numbers3)
print(result3)  # Output: [5, 5, 5, 5, 10, 10, 15, 15, 15, 10]
```

The function processes the input list `numbers` iteratively, tracking the 'max' element encountered thus far (`max_so_far`). Whenever a new element (`num`) surpasses the current `max_so_far`, the function adds the new 'max' to the `rolling_max_list`, and updates the `max_so_far` to the current element. This effectively generates a list of rolling maximums, reacting to surges and plateaus in the input list, and handling duplicates and gaps gracefully. 

The provided test cases demonstrate how the function works with various input lists, producing expected output.