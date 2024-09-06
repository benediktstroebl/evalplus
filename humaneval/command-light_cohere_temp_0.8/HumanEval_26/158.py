```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keeps elements elements left as in the input list
    """
    numbers = set(numbers)
    return [num for num in numbers if num not in numbers]

# Test case 1
test_data = [1, 2, 3, 2, 4]
test_result = remove_duplicates(test_data)
assert test_result == [1, 3, 4]

# Test case 2
test_data2 = [1, 1, 2, 3, 4, 4]
test_result2 = remove_duplicates(test_data2)
assert test_result2 == [1, 2, 3, 4]

# Test case 3
test_data3 = [1, 2, 3, 4, 5, 6]
test_result3 = remove_duplicates(test_data3)
assert test_result3 == [1, 2, 3, 4]
```
The function `remove_duplicates` is defined in this script, which accepts a list of integers as input and outputs a new list with any repeated values removed. The test cases demonstrate the