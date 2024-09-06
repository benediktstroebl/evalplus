```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ Removes all elements that occur more than once in a list of integers
        Returns a new list without duplicates, keeping the order of elements.
    """
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result
```

The algorithm works by initializing a set called `seen` to keep track of integers that have already appeared in the original list. Then, it iterates through each integer in the input list and checks if it exists in the `seen` set. If an integer is not in the set, it adds it to both the set and the result list. This way, the result list contains only unique integers, and the order is preserved from the original list.  This algorithm has a time complexity of O(n) since it requires iterating through the list once and performing constant time operations for set operations and list appending.