```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    max_count = 0
    current_max = numbers[0]
    max_list = [current_max]
    for num in numbers[1:]:
        if num > current_max:
            current_max = num
        elif num == current_max and max_count < len(numbers) - 1:
            max_count += 1
    max_list.return max_list.
# Example same. test cases:
print(rolling_max([1, 2, 3, 2, 3, 4, 2])))
print(rolling_max([1, 2, 3, 4, 5, 6, 7]))
```