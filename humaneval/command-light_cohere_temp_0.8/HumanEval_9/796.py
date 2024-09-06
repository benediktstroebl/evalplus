```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generates a list of rolling maximum elements from a given list of integers.
    Returns a list of maximum elements found in a specific order, where each element in the list is the maximum of 
    the numbers immediately preceding it until the given moment in the sequence.
    Input:
    list of integers
    """
    return [num for num, index in enumerate(numbers) if numbers[index] > numbers[index + 1] and index != len(numbers) - 1][0]]

test_rolling_max = [
    [1, 2, 3, 2, 3, 4, 2],
    [2, 3, 4, 5, 4, 3, 2],
    [2, 3, 4, 4, 3, 2, 1],
    [2, 3, 4, 3, 2, 1, 1],
    [2, 3, 4, 3, 2, 1, 2],
    [2, 3, 4, 3, 2, 3, 2],
    [2, 3, 5, 4, 3, 2, 1],
    [1, 2, 3, 4, 5, 6]
]

result = rolling_max(test_max)
for r, t in zip(result, test_max):
    print(r, t)
```