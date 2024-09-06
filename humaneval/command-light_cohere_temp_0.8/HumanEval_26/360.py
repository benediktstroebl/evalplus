```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Returns a unique elements in a new list.
    """
    unique = set(numbers)
    return [x for x in unique]

#Test case 1: [1, 2, 3, 2] should return [1, 2, 3]
test_remove_duplicates_case1 = [1, 2, 3, 2]
result1 = remove_duplicates(test_remove_duplicates_case1)
assert result1 == [1, 2, 3]

#Test case 2: [1, 2, 3] should return [1, 2, 3]
test_remove_duplicates_case2 = [1, 2, 3]
result2 = remove_duplicates(test_remove_duplicates_case2)
assert result2 == [1, 2, 3]

#Test case 3: [1, 3, 4] should return [1, 3, 4]
test_remove_duplicates_case3 = [1, 3, 4]
result3 = remove_duplicates(test_remove_duplicates_case3)
assert result3 == [1, 3, 4]

#Test case 4: [1, 2, 4, 3] should return [1, 2, 4]
test_remove_duplicates_case4 = [1, 2, 4, 3]
result4 = remove_duplicates(test_remove_duplicates_case4)
assert result4 == [1, 2, 4]

#Test case 5: [] should return []
test_remove_duplicates_empty = []
result5 = remove_duplicates(test_remove_duplicates_empty)
assert result5 == []
```
The function `remove_duplicates` takes a list of integers as input and returns a new list with unique elements. The test cases demonstrate the example usage of the function, and the expected results are compared with the actual results using the `assert` assertion.