```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    numbers.clip()
    roll(numbers)
    return [max(numbers) for i in range(len(numbers))]]

def roll(numbers: List[int]) -> None:
    for i, num in enumerate(numbers):
        numbers[i] = num + i + 1
    return numbers

# Test suite
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)
```