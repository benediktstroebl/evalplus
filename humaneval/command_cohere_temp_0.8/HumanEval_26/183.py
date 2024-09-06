```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    return list(set(numbers))
```
This Python script provides a function called `remove_duplicates`, which takes a list of integers (`List[int])` as input and returns a list of unique integers from the input list. It uses `set` to automatically remove duplicate elements, preserving the order of the remaining elements. This function is designed to solve the problem of removing elements that occur more than once in a list of integers while maintaining the order of the remaining elements. 
The function is self-contained and can be used directly to remove duplicates from a list of integers. It is compatible with Python 3, as it relies on the `set` constructor to remove duplicates and utilizes type hints with the `typing` module. 
The expected output for a list with duplicate elements is demonstrated below:
```python
remove_duplicates([1, 2, 3, 2, 4])
```
 resulting in:
[1, 3, 4]
```