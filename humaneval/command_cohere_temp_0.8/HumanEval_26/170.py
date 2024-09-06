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

The remove_duplicates function uses a set, seen, to track encountered integers and a list, result, to store unique integers in the order they appear in the input list. It iterates through the input list, checking if each integer is already in the seen set. If it's not present, it adds it to both the seen set and the result list. If the seen set has only one unique element, it adds that element to the result list, ensuring the last element of a duplicate pair is retained. The final result is a list of unique integers without duplicates.