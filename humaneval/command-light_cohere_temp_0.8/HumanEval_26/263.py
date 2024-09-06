```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    Remove elements that occur more than once from the input list.
    Args:
        numbers: list of integers
    Returns:
        list of integers without duplicates
    """
    set(numbers)
    return [i for i in numbers if i not in set(numbers)]

# Test case 1
test_case1 = [1, 2, 3, 2, 4]
print(remove_duplicates(test_case1))

# Test case 2
test_case2 = [1, 1, 2, 3]
print(remove_duplicates(test_case2))

# Test case 3
test_case3 = [3, 2, 4, 3, 5]
print(remove_duplicates(test_case3))

# Test case 4
test_case4 = [1, 2, 2, 3, 4, 5]
print(remove_duplicates(test_case4))
```
This Python script defines a function called `remove_duplicates` that takes a list of integers as input and returns a new list with duplicate elements removed. The function uses the important built-in set data type to remove any duplicate elements from the input list.