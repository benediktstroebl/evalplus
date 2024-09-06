```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [x for x, i in zip(numbers, numbers[1:])][::-1]
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # [1, 2, 3, 3, 3, 4, 4]
numbers = [1, 2, 3, 4, 5, 6, 7]
print(rolling_max(numbers))  # [5, 7, 6, 7]
``` 
The function uses the Python list comprehension to find the rolling maximum elements. This solution does a first in Python, and can be easily extended to other data structures that support list comprehensions.