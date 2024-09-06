```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    # Initialize Set of unique numbers
    seen = set()
    result = []

    # Iterate over the input list
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)

    return result
```

The function **remove_duplicates** takes a list of integers as input and returns a new list with all distinct integers. It achieves this by first converting the list into a set, which automatically eliminates duplicates, and then converts the set back into a list.