```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    numbers = list(numbers)
    n = len(numbers)
    max_num = numbers[0]
    start = 0
    ending = n - 1
    result = [max_num]
    
    while start <= ending:
        current_max = numbers[start]
        max_num = max(current_max, max_num)
        result.append(max_num)
        start += 1
    
    return result

# Test cases using the rolling_max function
numbers_list = [1, 2, 3, 2, 3, 4, 2]
test_result = rolling_max(numbers_list)
print(test_result)  # Output: [1, 2, 3, 3, 3, 4, 4]

numbers_list2 = [5, 2, 8, 1]
test_result2 = rolling_max(numbers_list2)
print(test_result2)  # Output: [8, 1]
```