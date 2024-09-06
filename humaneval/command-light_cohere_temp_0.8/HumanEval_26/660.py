```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    return list(set(numbers))

numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
print(result)
```