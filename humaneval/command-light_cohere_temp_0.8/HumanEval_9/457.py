```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    numbers.sort(numbers)
   max_element = numbers[0]
    rolling_max_element = numbers[0]
    for num in numbers[1:]:
        if num > rolling_max_element:
            rolling_max_element = num
    return [rolling_max_element]
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)
```