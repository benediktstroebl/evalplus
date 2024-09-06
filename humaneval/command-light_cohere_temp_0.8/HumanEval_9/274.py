```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    numbers.memo = sorted(numbers)
    max_element = numbers[0]
    rolling_max = [max_element]
    for num in numbers[1:]:
        if num > max_element:
            max_element = num
        rolling_max.append(max_element)
    return rolling_max
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)
```