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

The approach used in the function `remove_duplicates` is to iterate over the input list `numbers` and maintain a set called `seen` to keep track of unique elements. For each element `num` in the list, it checks whether it has been seen before (`num not in seen`) or whether it's the first occurrence of an element in the list (`len(seen) == 1`). If either of these conditions is true, it adds the element to the result list and updates the `seen` set. This way, elements that occur more than once get excluded from the result.

The expected output for a test case like `[1, 2, 3, 2, 4]` would be `[1, 3, 4]`.