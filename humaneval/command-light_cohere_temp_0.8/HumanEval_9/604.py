```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generates a list of rolling max elements from a given list of integers.
    >>> test_rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    numbers = List(sorted(numbers))
    result = [x for x in numbers if x == max(numbers[numbers.count(x):0])
    return result
``` 
The problem is to find the rolling maximum element in a list of integers. The solution is to create a new list of rolling maximum elements by counting the occurrences of each element in the original list.