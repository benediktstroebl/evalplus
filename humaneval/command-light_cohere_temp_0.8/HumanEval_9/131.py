```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    max_so_far = num = numbers[0]
    result = [num]
    for num in numbers[1:]:
        if num > max_so_far:
            max_so_far = num
        result.append(max_so_far)
    return result
 
# Test cases
numbers1 = [1, 2, 3, 4, 5]
numbers2 = [2, 3, 4, 5, 6]
print(rolling_max(numbers1))  # Expected Output: [1, 2, 3, 3, 4, 5]
print(rolling_max(numbers2))  # Expected Output: [2, 3, 4, 5]
```