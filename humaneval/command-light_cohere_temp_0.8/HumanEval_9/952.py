```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    numbers.len = len(numbers)
    max_num = numbers[0]
    max_num_idx = 0
    for i, n in enumerate(numbers):
        if n > max_num:
            max_num = n
            max_num_idx = i + 1
    return [max_num for _ in range(max_num_idx)]

numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)  # Expected output: [1, 2, 3, 3, 3, 4, 4]
```

This Python function, `rolling_max`, uses a list of integers and returns a new list containing the rolling maximum elements found in the input sequence. The `typing` module is used to define the function signature and ensure type correctness.