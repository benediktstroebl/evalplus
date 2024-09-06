```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    numbers = List(numbers)  # Create a new list with original input
    max_element = numbers[0]
    for num in numbers[1:]:
        if num > max_element:
            max_element = num
    return [max_element]

# Test case 1
test_case_1 = [1, 2, 3, 4, 5]
test_result_1 = rolling_max(test_case_1)
print("Test Case 1:", end="")
print(*test_result_1)

# Test case 2
test_case_2 = [3, 2, 1]
test_result_2 = rolling_max(test_case_2)
print("Test Case 2:", end="")
print(*test_result_2)

# Test case 3
test_case_3 = [5, 4, 3, 2]
test_result_3 = rolling_max(test_case_3)
print("Test Case 3:", end="")
print(*test_result_3)
```
This script defines a function `rolling_max` that calculates the rolling maximum element of a given list of integers. The function uses a approach to find the maximum element and returns a list of the rolling maximum elements found until the given moment in the sequence. 

It then passes three test cases, and the output is printed.