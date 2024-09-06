```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    max_num = numbers[0]
    max_index = 0
    for i, num in enumerate(numbers):
        if num > max_num:
            max_num = num
            max_index = i + 1
    return [max_num]

# Test case 1
test_case_1 = [1, 2, 3, 4, 5]
test_result_1 = rolling_max(test_case_1)
print("Test Case 1:", endswith(')')" + test_result_1)

# Test case 2
test_case_2 = [1, 1, 2, 3, 4]
test_result_2 = rolling_max(test_case_2)
print("Test Case 2:", endswith(')')" + test_result_2)

# Test case 3
test_case_3 = [1, , , 4]
test_result_3 = rolling_max(test_case_3)
print("Test Case 3:", endswith(')')" + test_result_3)

# Test case 4
test_case_4 = [2, 3, 4, 3, 2]
test_result_4 = rolling_max(test_case_4)
print("Test Case 4:", endswith(')')" + test_result_4)

# Test case 5
test_case_5 = [1, 1, 2, 3, 4, 5]
test_result_5 = rolling_max(test_case_5)
print("Test Case 5:", endswith(')')" + test_result_5)
```
This Python script defines a function `rolling_max` that calculates the rolling maximum element in a list of integers. The `typing` module is used to provide type hints for the function parameters and return values. The test cases aim to verify the functionality of the `rolling_max` function by passing different lists of integers.

You can uncomment the last five lines to run these tests and see the results.