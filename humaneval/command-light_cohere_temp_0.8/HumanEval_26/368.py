```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    Remove duplicates from the list.
    :type numbers : List[int]
    return: List[int]
    """
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return result
```
The `remove_duplicates` function removes duplicate elements from the `numbers` list, which is passed as a parameter. The function uses a `set` data structure to keep track of elements that have already been encountered. It iterates through elements from the `numbers` list and uses the `add` method of the `seen` set to add elements that are not duplicates. Finally, it appends each non-duplicate element to the `result` list and returns the modified list.