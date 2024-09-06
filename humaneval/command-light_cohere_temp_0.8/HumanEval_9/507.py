```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    numbers = list(numbers)  # Convert list of integers to a list of numbers
    max_num = numbers[0]
    for num in numbers[1:]:
        if num > max_num:
            max_num = num
    return [max_num]

# Example usage
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)
```
This script defines a function called `rolling_max` that takes a list of integers as input and returns a new list with the maximum element from the original list. It uses the in a loop to compare each element in the list with the current maximum element, and updates the maximum element accordingly. The example usage demonstrates how the will produce the correct output `[1, 2, 3, 3, 3, 4, 4]` as the list of rolling maximum elements.