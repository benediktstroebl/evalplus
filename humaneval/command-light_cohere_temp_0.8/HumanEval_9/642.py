```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    return [max(numbers[i:j]) for i, j in zip(range(len(numbers)), range(j + 1)) if j < len(numbers))]

# Test cases for rolling_max function
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)  # Output: [1, 2, 3, 3, 3, 4, 4]
``` 
This Python function, rolling_max, takes a list of integers as input and returns a list of the maximum elements found as they roll through the sequence. This is method uses the common Python approach, where it generates a new list by sliding over the existing list.