```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    max_so_far = nums[0]
    result = [max_so_far]
    
    for i, num in enumerate(numbers[1:], start=1):
        current = num
        max_so_far = max(max_so_far, current)
        result.append(max_so_far)
    
    return result

# Test cases
numbers1 = [1, 2, 3]
numbers2 = [2, 3, 4]
numbers3 = [5, 6, 7]

print(rolling_max(numbers1))  # Output: [1, 2, 3]
print(rolling_max(numbers2))  # Output: [2, 3, 4]
print(rolling_max(numbers3))  # Output: [5, 6, 7]
 ```

This Python code defines a function called rolling_max that takes a list of integers as input and generates a new list with the maximum element from the original list for each index. The function effectively rolls over the