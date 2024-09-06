```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Return a list of rolling maximum elements found in the given list.
    Args: 
        numbers: list of integers
    Returns: 
        list of integers, the rolling maximum elements found in the given list.
    """
    def rolling_max(numbers):
        numbers = sorted(numbers)
        result = [x for x in numbers if x != numbers[-1]]
        result += [numbers[i] for i in range(1, len(numbers))]
        return result

# Unit tests
numbers = [1, 2, 3, 4, 3, 5]
result = rolling_max(numbers)
print(result)
```