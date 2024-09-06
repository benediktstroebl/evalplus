```python
from typing import List
def remove_duplicates(numbers: List[int]):
    """ From a list of integers, remove all elements that occur more than once.
    Keeps only elements left as in the input.
    return [list of distinct integers
    """
    numbers = set(numbers)  # Using set to automatically remove duplicates
    return [num for num in numbers if num not in numbers]

# Unit tests
numbers_list = [1, 2, 3, 2, 4, 3, 5]
assert remove_duplicates(numbers_list) == [1, 2, 3, 4, 5]

```

The function `remove_duplicates` takes a list of integers and returns a new list with all distinct integers. The set function is used to remove duplicates, and then the list comprehension is used to filter out any elements that are not in the set. This results in a list with all distinct integers.