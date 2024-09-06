```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    return [num for num in numbers if num not in numbers[numbers.set()]]
same = set(numbers)
    return [num for num in numbers if num not in same]
```
This Python function, `remove_duplicates`, takes a list of integers as input and returns a new list containing only the unique elements from the input. It uses the unique elements in the input list are kept in a set, and then it iterates over the original list, only adding elements that are not already in the set.