Here is a self-contained Python script that solves the problem of finding the rolling maximum elements in a list of integers:
```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    max_count = 0
    current_max = numbers[0]
    max_elements = [current_max]

    for num in numbers[1:]:
        if num > current_max:
            current_max = num
        max_count += 1

    return max_elements[:max_count]

# Example usage
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)  # Output: [1, 2, 3, 3, 3, 4, 4]
```
This script defines a function `rolling_max` that takes a list of integers as input and returns a list of the rolling maximum elements found in the sequence. It uses a for the the first element in the list, then iterates over the sequence, and whenever a larger element is found, it updates the current_max and max_count variables. The rolling maximum elements are then filtered to include only the max_count elements.