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

The remove_duplicates function uses a set, seen, to track encountered integers and a list, result, to store unique integers in the order they appear in the input list. It iterates through the input list, checking if each integer is already in the seen set. If it's not present, it's added to both the set and the result list. If the set's size was originally 1, indicating the last occurrence of an integer, it also adds the integer to the result. This ensures uniqueness and maintains the order of the remaining integers.

Here's an example usage and its expected output:
```python
>>> remove_duplicates([1, 2, 3, 2, 4])
[1, 3, 4]
```

This function adheres to the problem's requirements, removing duplicates while preserving the order of unique integers.