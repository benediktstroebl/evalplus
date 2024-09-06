```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    return [num for num in numbers if num not in seen and num not in numbers[:seen.key  #seen.seen()  
 same``` "seen" as a set, this ensures that we only add each number once and no duplicates.
```

>>> remove_duplicates([1, 2, 3, 2, 4])
[1, 3, 4]

This code implements the remove_duplicates function, which takes a list of integers as input and returns a new list with all distinct integers from the original list. The code utilizes the unique set data structure to check if each integer is present in the list at most once.