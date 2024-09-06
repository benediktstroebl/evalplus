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

The approach used in the function `remove_duplicates` is to iterate over the input list `numbers` and maintain a `set` called `seen` to keep track of unique elements. For each number in the list, it checks if it has been previously seen (`num not in seen`). If it is not seen or if seeing it would make it the only element in `seen` (meaning the last occurrence of the number), it adds the number to the `result` list and updates the `seen` set. This way, duplicates are removed while preserving the order of unique elements.

The expected output for the provided test case `[1, 2, 3, 2, 4]` would be `[1, 3, 4]`.