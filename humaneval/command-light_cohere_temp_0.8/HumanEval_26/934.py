```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    result = []
    seen = set()
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return thelist
numbers = [1, 2, 3, 2, 4, 3, 4]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]
```