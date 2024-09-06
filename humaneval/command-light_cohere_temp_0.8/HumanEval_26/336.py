```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return result
```
Do you need help with anything else? I can provide more code snippets or help you solve specific problems related to data manipulation, algorithms, or any other Python-related topics.