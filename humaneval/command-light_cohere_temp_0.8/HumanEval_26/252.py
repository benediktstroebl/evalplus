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

This code defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with all distinct integers. The function uses a set data structure to keep track of seen numbers and a new list to store the unique elements. The function iterates through the `numbers` list and adds all the elements to the `result` list if they are not already in the `seen` set. This process effectively removes duplicates from the list and returns the new list.