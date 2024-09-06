```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    numbers.sort()
    max_num = numbers[0]
    rolling_maxes = [max_num]
    for num in numbers[1:]:
        if num > max_num:
            max_num = num
        rolling_maxes.append(max_num) 
    return rolling_maxes
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)
```