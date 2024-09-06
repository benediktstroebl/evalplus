```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ Removes all elements that occur more than once in a list of integers
        Keeps order of elements left the same as in the input """
    seen = set()
    result = [x for x in numbers if not (x in seen or seen.add(x))]
    return result
```

This Python script defines a function called `remove_duplicates` which takes a list of integers as input. It removes all elements that occur more than once from the given list and returns a new list containing only the unique elements. The function uses a set called `seen` to keep track of the unique elements encountered while iterating through the input list. By using a set, the elements are automatically removed if they occur more than once, ensuring that only unique elements are added to the result list. The result list is then returned, preserving the original order of the first occurrences of the unique elements.  This approach has a time complexity of O(n) since it requires iterating through the input list once and performing a constant-time operation for set membership checks.