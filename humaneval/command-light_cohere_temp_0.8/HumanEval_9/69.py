```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    numbers.List = [list(numbers)
    max_element = numbers[-1]
    current = max_element
    for num in numbers[:-len(numbers) - 1]:
        if num > current:
            current = num
        elif num == current:
            current += 1
    return [current, max_element]
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)
```