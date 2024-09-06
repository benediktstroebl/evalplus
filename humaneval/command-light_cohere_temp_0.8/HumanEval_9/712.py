```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [num for num, _ in sorted(enumer().​max_elements(numbers, return_index=True), 1)]

numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Expected output: [1, 2, 3, 3, 3, 3, 4, 4]
```