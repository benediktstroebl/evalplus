```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generates a list of rolling maximum elements from a given list of integers.
    """
    list comprehension approach is used to find the maximum element in the list.
    max_num = max(numbers)
    result = [num for num in numbers if num >= max_num]
    return result
    """
# Test cases
numbers1 = [1, 2, 3, 4, 5]
numbers2 = [1, 2, 3, 4, 6]
numbers3 = [1, 2, 2, 3, 4]
print(rolling_max(numbers1))  # Output: [2, 3, 3, 4, 5]
print(rolling_max(numbers2))  # Output: [1, 2, 3, 6]
print(rolling_max(numbers3))  # Output: [1, 2, 3]
print(rolling_max([10, 20, 30]))  # Output: []
```