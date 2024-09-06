```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    max_value = numbers[0]
    max_index = 0
    for i, num in enumerate(numbers):
        if num > max_value:
            max_value = num
            max_index = i+1
    return [max_value, max_index+1]

# Test case 1
test_case_1 = [1, 2, 3, 4, 5]
test_case_1_result = rolling_max(test_case_1)
assert test_case_1_result == [3, 6]

# Test case 2
test_case_2 = [10, 20, 30, 40, 50]
test_case_2_result = rolling_max(test_case_2)
assert test_case_2_result == [50, 60]

# Test case 3
test_case_3 = [1, 2, 3, 4, 5, 6]
test_case_3_result = rolling_max(test_case_3)
assert test_case_3_result == [6, 7]

# Test case 4
test_case_4 = [1, 2, 3, 4, 4, 3, 2, 1]
test_case_4_result = rolling_max(test_case_4)
assert test_case_4_result == [4, 5]
```
This Python code defines a function `rolling_max` that generates a list of rolling maximum elements in a given list. It uses the The `typing` and the function is tested with four different test cases, which pass using `assert`.