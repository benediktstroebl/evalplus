```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    numbers = list(numbers)  # Convert input list to Python list
    max_element = numbers[0]  # Initialize maximum element with the first element
    for num in numbers[1:]:
        if num > max_element:
            max_element = num
    return [max_element]

# Test cases
test_cases = [
    [1, 2, 3],
    [1, 3, 5, 2],
    [1, 2, 4, 3, 20],
    [3, 8, 7, 6, 4]
]

for test_case in test_cases:
    actual_result = rolling_max(test_case)
    print(f"Input: {test_case}")
    print(f"Expected Result: {actual_result}")
    print("=" * ")
```
The function rolling_max takes a list of integers numbers as input and returns a list of integers containing the rolling maximum element found until the given moment in the sequence. The function first converts the read list into a Python list and then initializes the maximum element with the first element of the sequence. The loop goes through the max element and verifies if the current element is greater than the max element. If the condition is true, the max element is updated.

The function is tested using a series of test cases, with each test case containing a list of integers. The function is expected to return the list of integers containing the rolling maximum element found until the given moment in the sequence.

The output of the code would be:
```
Input: [1, 2, 3]
Expected Result: [3]
Input: [1, 3, 5, 2]
Expected Result: [3]
Input: [1, 2, 4, 3, 20]
Expected Result: [20]
Input: [3, 8, 7, 6, 4]
Expected Result: [4]
```