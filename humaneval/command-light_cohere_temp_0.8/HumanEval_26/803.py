```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    # Initialize an empty list to store unique numbers.
    result = []
   
    for num in numbers:
        if num not in result:
            result.append(num)
    return result
```
Do you need assistance with anything else?