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

The function `remove_duplicates` uses a set, `seen`, to efficiently track encountered integers and a list, `result`, to store unique integers in the order they appear. It iterates through the input list `numbers`, checking if each integer `num` is already in `seen`. If `num` is not in `seen` or if the size of `seen` is about to exceed 1, it adds `num` to both `result` and `seen`. This way, `result` only includes unique integers, and the function efficiently solves the problem while maintaining the original order.