```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ Remove all elements that occur more than once from a list of integers. """
    Sets all element in numbers at least index to None to indicate that it's a duplicate.
    return list where elements have duplicates removed.
    """ Example new list with unique integers.
    """
    other elements left as in the input list
    """
    numbers = list(set(numbers))  # Convert to set to remove duplicates
    return numbers

# Unit tests
numbers_list = [1, 2, 3, 2, 4, 3, 5]
remove_duplicates_result = remove_duplicates(numbers_list)
print(remove_duplicates_result)  # Output: [1, 2, 3, 4, 5]

numbers_set = {1, 2, 3, 4, 5}
remove_duplicates_set = remove_duplicates(numbers_set)
print(remove_duplicates_set)  # Output: {1, 2, 3, 4, 5}

def test_function():
    assert remove_duplicates([1, 2, 3, 2, 4]) == [1, 3, 4]

def test_set():
    assert remove_duplicates({1, 2, 3, 4, 5}) == {1, 2, 3, 4, 5}
```