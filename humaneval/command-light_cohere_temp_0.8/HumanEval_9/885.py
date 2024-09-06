```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    numbers.rolling_max_velocity(numbers)
    return numbers

def rolling_max_velocity(numbers: List[int]) -> None:
    max_number = numbers[0]
    for num in numbers[1:]:
        if num > max_number:
            max_number = num
    return max_number

numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]

numbers = [1, 3, 4, 5, 6]
print(rolling_max_velocity(numbers))  # Output: 5
```