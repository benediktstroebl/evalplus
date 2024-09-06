```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ 
    Remove all elements that occur more than once from a list of integers.
   
    """ Return a list of numbers leaving only the first occurrence of each number.
    """
    removing duplicates:
    [1, 2, 3, 2, 4] -> [1, 3, 4]
    """
    return [x for x in numbers if x not in set(numbers)]

# Test case 1: Single occurrence numbers
test_remove_duplicates_single = [1, 2, 3, 2]
result_single = remove_duplicates(test_remove_duplicates_single)
assert result_single == [1, 2, 3]

# Test case 2: Multiple occurrences numbers
test_remove_duplicates_multiple = [1, 1, 2, 3, 2, 4]
result_multiple = remove_duplicates(test_remove_duplicates_multiple)
assert result_multiple == [1, 2, 3, 4]

print("All tests passed!")
```