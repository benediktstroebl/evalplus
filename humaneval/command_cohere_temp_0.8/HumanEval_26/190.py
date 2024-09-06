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

The approach used in the function `remove_duplicates` is to iterate through the list of numbers, and for each number, add it to the result list if it hasn't been seen before or if it's the second time we've seen it (indicating there's only one duplicate). This ensures the correct removal of duplicates while maintaining the order of unique elements.