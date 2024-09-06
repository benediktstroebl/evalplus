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

The remove_duplicates function uses a set, seen, to track encountered integers and a list, result, to store unique integers in the order they appear in the input. It iterates through the input list, checking if each integer is already in the seen set. If it's not, or if it's the first encountered occurrence of that integer, it adds the integer to both the result and seen sets. This ensures that only unique integers are retained in the result list, and their order matches the input's.