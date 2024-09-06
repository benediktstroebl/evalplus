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

This Python script defines a function called `remove_duplicates` that takes a list of integers as input. It removes any elements that occur more than once from the input list and returns a unique list of integers in the same order as the input list. 

The function uses a set called `seen` to keep track of elements that have already been encountered. As it iterates through the input list, each element that is not in the `seen` set is added to both the set (to mark it as seen) and the `result` list (to retain the original order). Elements that are encountered more than once are ignored and do not appear in the final `result` list. 

The script ensures that the same problem is solved as outlined in the original problem statement. It also maintains the original order of elements in the input list in the final unique list. 

This code can be imported and used anywhere in a Python project and is also reusable as it is self-contained within a single Python file with the necessary type annotations and comments for better understanding.