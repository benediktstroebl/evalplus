Here's the self-contained Python function:
```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    max_number = numbers[0]
    for num in numbers[1:]:
        max_number = max(max_number, num)
    return [max_number]

# Test case 1
test_case_1 = [1, 2, 3, 4, 5]
test_result_1 = rolling_max(test_case_1)
print(test_result_1)

# Test case 2
test_case_2 = [5, 4, 3, 2, 1]
test_result_2 = rolling_max(test_case_2)
print(test_result_2)
```
This function, `rolling_max`, takes a list of integers as input and uses a loop to find the maximum element in the list. The function then returns the maximum element.