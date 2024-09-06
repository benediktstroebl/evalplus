```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ Removes all elements that occur more than once in a list of integers
        Returns a new list without any duplicates, keeping the order of elements left as is.
    """
    seen = set()
    result = []
    for num in numbers:
        if num not in seen and not seen.add(num):
            result.append(num)
    return result
```

The algorithm utilizes a set `seen` to keep track of logged integers. The `result` list is filled with integers only if they have not been previously seen and can be added to `seen`. This ensures the list's uniqueness, while the order is preserved as the elements are directly appended to the `result` list.