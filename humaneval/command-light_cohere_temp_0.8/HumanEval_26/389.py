```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ Removes duplicates from a list of integers.
    @param numbers: list of integers
    @return: list of integers without duplicates
    """
    return [num for num in numbers if num not in numbers[numbers.count(num)]


# Unit tests
numbers = [1, 2, 3, 2, 4, 2, 3, 1]
test_remove_duplicates = remove_duplicates(numbers)
assert test_remove_duplicates == [1, 2, 3, 4]

numbers = [1, 1, 2, 2, 2]
test_remove_duplicates = remove_duplicates(numbers)
assert test_remove_duplicates == [1, 2]

numbers = [1, 1, 2, 3, 4, 3]
test_remove_duplicates = remove_duplicates(numbers)
assert test_remove_duplicates == [1, 3, 4]
```