```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    return [n for n, i in zip(sorted(numbers), range(len(numbers))) if i < len(numbers)]
```
This solution employs a list comprehension with the zip function to pair each element with its index, followed by a filtering condition with the index and the length of the list. The final list will contain the each element as its respective maximum value, achieved by the condition.