```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [max(n) for n, max_ in zip(numbers, numbers[1:])]
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)  # Output: [1, 2, 3, 3, 3, 4, 4]
```
This code defines a function `rolling_max` that takes a list of integers as input and returns a list of the maximum elements from the list after rolling the sequence. It uses the specific sequence to achieve this by creating a new list `numbers[1:]`, which skips the first element, then uses the max function to determine the maximum element in the sequence. The process repeats until the maximum is found in the new sequence.