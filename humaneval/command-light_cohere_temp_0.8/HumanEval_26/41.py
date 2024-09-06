```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    result = [num for num in numbers if num not in seen and num < seen]
    seen.add(numbers)
    return result

test_remove_duplicates = []
test_remove_duplicates.append([1, 2, 3, 2])
test_remove_duplicates.append([4, 4, 3])

print("Results:", remove_duplicates(test_remove_duplicates))
```