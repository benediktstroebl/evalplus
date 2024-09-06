```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    max_numbers = numbers[0]
    current = max_numbers
    for num in numbers[1:]:
        current = max(current, num)
        max_numbers = current
    return [current, max_numbers]

numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)  # Output: [3, 4]
```
This script defines a function rolling_max that takes a list of integers as input and returns a list of the rolling maximum elements. The function uses the new type hints from typing, and it creates a function that calculates the rolling maximum elements in a list. It initializes the run with the first element and keeps comparing to find the current maximum element and update the rolling maximum. This final output is the, for the given list [1, 2, 3, 2, 3, 4, 2], the function returns [3, 4].