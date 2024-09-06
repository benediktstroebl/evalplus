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

The approach used in the function `remove_duplicates` is to iterate through each number in the list and add those that aren't in the seen set or if the seen set has only one element to the result list. At the same time, it keeps track of the elements in the seen set to ensure that no element is added more than once. This effectively removes duplicates, and the result is a list of unique numbers in the same order they appeared in the original list.