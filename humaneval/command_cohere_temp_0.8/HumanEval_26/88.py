```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    result = []
    for num in numbers:
        if num not in seen or len(seen) == 1:
            result.append(num)
            seen.add(num)
    return result
```

The function `remove_duplicates` removes elements that occur more than once in a list of integers, while preserving the order of the remaining elements. It does so by utilizing a set, `seen`, to keep track of the elements that have already been encountered. As sets only store unique elements, any repeated elements are automatically removed from the set as they are added. This set is then used to filter the original list, only adding elements that aren't already in the set (i.e., not repeated) or if the set has only one element (i.e., the very first occurrence of an element). The function returns the new list, which contains only the unique elements, in their original order.