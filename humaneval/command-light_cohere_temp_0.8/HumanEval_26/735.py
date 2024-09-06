Here's a self-contained Python function that removes duplicates from a list of integers and passes the test:

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

This function utilizes a set to keep track of unique elements and then stores the remaining, non-repeated integers in a new list. The function can accept any list of integers as input and returns a new list with no duplicates.