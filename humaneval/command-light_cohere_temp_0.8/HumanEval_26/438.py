```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    return [num for num in numbers if num not in set(numbers)]

# Unit tests
numbers_list = [1, 2, 3, 2, 4, 2, 3, 5]
test_remove_duplicates(numbers_list)

numbers_set = {1, 2, 3, 4, 5}
test_remove_duplicates(numbers_set)

set_of_nums = {1, 2, 2, 3, 4, 5, 6}
test_remove_duplicates(set_of_nums)

def test_remove_duplicates_empty(numbers: List[int]):
    return numbers == []
test_remove_duplicates_empty([])
```
The provided Python script defines a function `remove_duplicates` that takes a list of integers as input and returns a new list containing only the unique elements. The function uses a method of generating the set of all elements in the input list, and then checks if each number in the original list is not already present in the set. This ensures that the only the duplicates are removed from the list.

The script also includes unit tests for the `remove_duplicates` function using test functions and sample inputs.