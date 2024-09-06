```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return [result])
    return result

# Unit tests
numbers_list = [1, 2, 3, 2, 4, 3, 1, 5, 4]
result_ref = [1, 3, 4]
assert remove_duplicates(numbers_list) == result_ref

print("All tests passed!")
```