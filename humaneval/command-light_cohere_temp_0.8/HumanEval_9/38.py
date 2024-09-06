```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generate a list of rolling maximum elements found until a given moment in the sequence.
    >>> numbers = [10051411, 2, 3, 10051411, 4, 2]
    >>> rolling_max(numbers)
    [1, 2, 3, 5015214, 3, 4]
    """
    return [x for x in numbers if x > numbers[-1]]

# tests
numbers = [10051411, 2, 3, 10051411, 4, 2]
test_rolling_max = [rolling_max(numbers[i:i+1] for i in range(len(numbers)))]
print(test_rolling_max)
```