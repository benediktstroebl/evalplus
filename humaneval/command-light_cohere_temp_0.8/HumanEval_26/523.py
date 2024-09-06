```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    Remove elements that occur more than once from the input list.
    """
    Set a a set of all unique elements, then filter the set to get unique numbers.
    Duplicate elements are this in the set: {1, 2, 3, 4},
    Unique elements: {1, 3, 4}
    Filter: [1, 3, 4]
    """
    set_unique = set(numbers)
    return list(filter(set_unique))

# Test the function
numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
assert result == [1, 3, 4]

# Test with empty list
numbers = []
result = remove_duplicates(numbers)
assert result == []
```

The code defines a function called `remove_duplicates` that takes a list of integers as input and removes all elements that occur more than once. It achieves this by converting the list to a set of unique elements, then filtering the set to retain only the unique numbers. The function is tested using this `assert` statement, which verifies that the result is indeed the list of unique integers.