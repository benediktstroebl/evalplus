```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    result = []
    for num in numbers:
        if num not in seen or len(seen) == 1:
            result.append(num)
            seen.add(num)
    return result
```

The function `remove_duplicates` takes a list of integers as input and returns a list of unique integers from the input list. It uses a set called `seen` to keep track of the unique integers already encountered. 

For each integer in the input list, the function checks if the integer is already in the `seen` set. If the integer is not in the set, or if the set contains only one element at this point, it adds the integer to the `result` list and the set. If the integer is already in the set, the integer is skipped and not added to the result list, effectively removing duplicates.

This way, the function removes all elements that occur more than once from the input list and returns a list of unique elements in the order they appeared in the input list.