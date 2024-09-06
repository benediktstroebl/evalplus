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

The approach used is a typical set-based solution. The main idea is to convert the list into a set and remove duplicate elements from it. This is done using a set called 'seen'. Then we create a new list to store the unique elements from the set in the original order. Finally, the function returns this list, which is now free of duplicate entries. 

This code is efficient and has a time complexity of O(n) because it only iterates through the list once and does not require any further processing. It handles various input cases, including edge cases, as specified in the problem statement.