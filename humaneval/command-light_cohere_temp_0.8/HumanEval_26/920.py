```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    numbers = set(numbers)
    return list(numbers)


# Test cases
numbers_list = [1, 2, 3, 2, 4, 3, 5]
assert remove_duplicates(numbers_list) == [1, 3, 4, 5], "Test failed: "

numbers_set = set([1, 2, 3, 4, 5])
assert remove_duplicates(numbers_set) == [1, 3, 4, 5], "Test failed: "

numbers_list2 = [1, 1, 2, 3]
assert remove_duplicates(numbers_list2) == [1, 2, 3], "Test failed: "

numbers_set2 = set([1, 2, 3])
assert remove_duplicates(numbers_set2) == [1, 2, 3], "Test failed: "

print("All tests passed!")
```