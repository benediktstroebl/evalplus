```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    numbers = list(numbers)  # Convert the input list to a Python list
    return [max(numbers[i:i+1]) for i in range(len(numbers))]

numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)
```

The code defines a function called `rolling_max` that takes a list of integers as input and generates a new list of the rolling maximum elements found in that sequence. The function uses list comprehension to iterate through the sequence and finds the maximum element at each moment until the current index reaches the end of the sequence. The resulting list is then the maximum elements found throughout the sequence.