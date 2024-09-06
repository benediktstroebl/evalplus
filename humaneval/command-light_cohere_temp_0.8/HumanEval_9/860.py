```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    max_values = [x for x in numbers if x > numbers[-1]]
    max_index = max(max_values, key=max_values.max_values.max_index)difference)
    max_index
    return [max_values[max_index - 1], max_values[max_index]]

test_rolling_max = [
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 6],
    [1, 2, 3, 4],
]

result = rolling_max(test_rolling_max)
print(result)
```