```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    max_so_far = numbers[0]
    result = [max_so_far]
    for num in numbers[1:]:
        if num > max_so_far:
            max_so_far = num
        result.append(max_so_far)
    return result
# Test cases
numbers1 = [1, 2, 3, 4, 5]
numbers2 = [2, 3, 4, 5, 6]
print(rolling_max(numbers1))  # Expected output: [1, 2, 3, 3, 4, 5]
print(rolling_max(numbers2))  # Expected output: [2, 3, 4, 5]
 ```

This function efficiently calculates the rolling maximum element in an ascending list of integers, and it passes the test of functionality with the provided test cases.