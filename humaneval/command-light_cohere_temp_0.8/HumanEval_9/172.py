```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    max_numbers = List(numbers)
    current_max = max(max_numbers)

    for num in numbers[1:]:
        if num > current_max:
            current_max = num
    max_numbers = [num for num in max_numbers if num == current_max]
    return max_numbers
```