```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    numbers.sort(numbers)
   max_element = numbers[0]
    rolling_max_list = [max_element]
    for num in numbers[1:]:
        if num > max_element:
            max_element = num
    max_element_list = [max_element]
    rolling_max_list.append(max_element_list)
    return rolling_max_list
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)
```