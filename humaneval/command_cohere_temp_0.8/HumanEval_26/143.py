```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ Removes duplicates from a list of integers and returns the unique list in the same order. """
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result
```

This script defines a function called `remove_duplicates` which takes a list of integers as input and returns a list of unique integers. Inside the function, it uses a set called `seen` to keep track of seen integers and a list called `result` to store the unique integers. The function iterates over the input list, and for each integer, it checks if the integer is not in the seen set, adds it to both the set and the result list, and skips duplicates. Finally, it returns the result list of unique integers in the same order as the input list.