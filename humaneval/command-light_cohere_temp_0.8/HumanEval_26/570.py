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

This function, `remove_duplicates`, takes a list of integers as input and returns a new list with unique integers from the input list. It utilizes a `seen` set to keep track of seen numbers and uses a for loop to iterate through the input list. This function effectively removes any duplicate elements from the input list.