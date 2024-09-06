```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    Remove all elements that occur more than once from a list of integers.
    Returns a list with distinct integers.
    """
    function uses a List[int] because the order of elements is not important
    """
    numbers = list(set(numbers))
    return numbers

# Test case 1
test_list1 = [1, 2, 3, 2, 4]
test_result1 = remove_duplicates(test_list1)
assert test_result1 == [1, 3, 4]

# Test case 2
test_list2 = [1, 2, 3, 4, 3]
test_result2 = remove_duplicates(test_list2)
assert test_result2 == [1, 2, 3, 4]

# Test case 3
test_list3 = [1, 2, 3, 1]
test_result3 = remove_duplicates(test_list3)
assert test_result3 == [1, 2, 3]

# Test case 4
test_list4 = [10, 20, 30, 40]
test_result4 = remove_duplicates(test_list4)
assert test_result4 == [10, 20, 30, 40]

print("All tests passed!")
```