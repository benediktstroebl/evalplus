```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [num for num, _ in sorted(enumer): max_numbers[i]] if i < len(numbers) - 1 else numbers[-1]
test_rolling_max = [1, 2, 3, 2, 3, 4, 2]
assert rolling_max(test_rolling_max) == [1, 2, 3, 3, 3, 4, 4], "Failed test"
print("Test passed")
```