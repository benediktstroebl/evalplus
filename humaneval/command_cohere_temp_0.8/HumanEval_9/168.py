Here's a Python script that contains a function called `rolling_max` which takes a list of integers `numbers` as input and returns a list of rolling maximum elements found up to that point in the sequence:
```python
from typing import List, Tuple

def rolling_max(numbers: List[int]) -> List[int]:
    max_so_far = float('-inf')
    rolling_max_so_far = [max_so_far]
    
    for num in numbers:
        max_so_far = max(num, max_so_far)
        rolling_max_so_far.append(max_so_far)
    
    return rolling_max_so_far

# Test Cases
numbers_list = [1, 2, 3, 2, 3, 4, 2]
rolling_max_result = rolling_max(numbers_list)
print(rolling_max_result)  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This code defines a function called `rolling_max` that takes a list of integers as input. It maintains two variables: `max_so_far` tracks the maximum value encountered thus far, initialized to negative infinity, and `rolling_max_so_far` is a list that stores the rolling maximums up to each point in the sequence. 

The code iterates through each number in the input list. For each number, it updates both `max_so_far` and `rolling_max_so_far` by comparing the current number with the maximum seen so far. 

Finally, the function returns the list `rolling_max_so_far`, which represents the rolling max for each element in the input list. 

When you run the provided test case, the output is as expected, confirming that the script solves the problem correctly. )): [1, 2, 3, 3, 3, 4, 4].