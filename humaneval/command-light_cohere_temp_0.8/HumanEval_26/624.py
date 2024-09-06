```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ Remove elements that occur more than once from a list.
    return a list where elements are unique
    """
    numbers = set(numbers)  # Remove duplicates using set()
    return [x for x in numbers if x not in set(numbers)]
```
This function, `remove_duplicates`, takes a list of integers `numbers` as input and returns a new list with integers that are unique. It achieves this by using the set() function to remove duplicates from the input list and then uses a list comprehension to filter out any elements that are not in the set.