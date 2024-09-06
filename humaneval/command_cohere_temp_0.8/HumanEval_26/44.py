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

This code defines a function `remove_duplicates` that takes a list of integers as input and removes any elements that appear more than once in the list. It does this by using a set `seen` to keep track of elements that have been encountered before. As a set cannot store multiple occurrences of the same element, using it to track the elements that have been seen ensures that duplicates are automatically removed. Any element that is not in the set is appended to the `result` list, which stores the unique elements in the order they appeared in the input list. 

Here's an example of using this function:
```python
>>> remove_duplicates([1, 2, 3, 2, 4])
[1, 3, 4]
```