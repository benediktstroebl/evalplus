```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    max_numbers = [x for x in numbers if x == numbers[0]]
    for num in numbers[1:]:
        if num > max_numbers[0]:
            max_numbers[0] = num
        elif num > max_numbers[1]:
            max_numbers[1] = num
    return max_numbers

# Unit tests
numbers = [1, 2, 3, 4, 5]
expected = [1, 2, 3, 3, 3, 4]
result = rolling_max(numbers)
assert len(result) == len(expected)
assert result == expected
```