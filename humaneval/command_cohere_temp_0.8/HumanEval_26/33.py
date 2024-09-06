```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    return list(set(numbers))
```
This Python script defines a function called `remove_duplicates` that takes a list of integers as input. It uses a set to remove any duplicate elements from the input list and returns the unique elements as a list. This is a common data manipulation task in programming, and the script provides a concise solution using Python's built-in `set` data structure to achieve this.  This approach has a time complexity of `O(n log n)`, where `n` is the number of elements in the input list, due to the inherent efficiency of set operations in Python.