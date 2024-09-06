```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    A function that calculates the rolling max element in a list of integers.
    returns a max element(s) for each window of n numbers
    using a sliding window technique.
    """
    n = len(numbers)
    result = [num for num in numbers]
    for i in range(1, n):
        current = result[i - 1]
        if numbers[i] > current:
            result[i] = numbers[i]
        else:
            result[i] = current + 1
    return result
```