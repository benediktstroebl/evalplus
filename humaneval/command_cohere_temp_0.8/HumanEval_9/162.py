Here's a Python script that contains a function called `rolling_max` which takes a list of integers `numbers` as input and returns a list of rolling maximum elements found at every point in the sequence:
```python
from typing import List, Tuple

def rolling_max(numbers: List[int]) -> List[int]:
    max_so_far = numbers[0]
    max_list = [max_so_far]
    
    for idx, number in enumerate(numbers[1:]):
        if number > max_so_far:
            max_so_far = number
            max_list.append(max_so_far)
        max_list[idx + 1] = max_so_far
    
    return max_list

# Test Cases
numbers_test_case_1 = [1, 2, 3, 2, 3, 4, 2]
numbers_test_case_2 = [1, 2, 2, 3, 4, 3, 2, 1]

test_case_1_result = rolling_max(numbers_test_case_1)
test_case_2_result = rolling_max(numbers_test_case_2)

assert test_case_1_result == [1, 2, 3, 3, 3, 4, 4], "Test case 1 failed."
assert test_case_2_result == [1, 2, 3, 4, 4, 4, 2, 2], "Test case 2 failed."
```

This script utilizes a rolling maximum algorithm, where you only need to keep track of the maximum value found so far (`max_so_far`) and the list of maximum values at each point (`max_list`).