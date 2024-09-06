```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    return [num for num in numbers if num not in seen and num not in numbers[seen:add(num,seen)]]

numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
print(result)
```