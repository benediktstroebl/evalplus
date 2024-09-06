```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep the duplicate elements left as in the input list.
    """
    duplicates are any of the set(numbers)
    new_list = [num for num in numbers if num not in set(numbers)]
    return new_list
```