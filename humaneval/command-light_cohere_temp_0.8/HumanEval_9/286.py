```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [x for x, i in zip(numbers, numbers[1:]) if i < len(numbers) and numbers[i] > numbers[i-1]]

# Example test cases
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Expected output: [1, 2, 3, 3, 3, 4, 4]

numbers = [1, 3, 2, 4, 5]
print(rolling_max(numbers))  # Expected output: [1, 3, 4, 5]

numbers = [10, 20, 30, 40, 50]
print(rolling_max([x for x in numbers if x % 2 == 0]))  # Expected output: [10, 30, 40]
```