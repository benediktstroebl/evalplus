```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return theresult
```

This function utilizes a set to track unique integers. The function then loops through the input list and adds integers to the set if they are not already present. If an integer is added to the set, it is assumed to be duplicated and is added to the result list.