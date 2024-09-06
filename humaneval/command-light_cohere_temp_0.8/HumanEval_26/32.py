```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ 
    Remove elements that occur more than once from the list.
    Args: 
    - numbers (List[int]): list of integers 
    Returns: 
    - A list of integers without duplicates 
    """
    return [x for x in numbers if x not in numbers[numbers.set()]]


tests = [
    [1, 2, 3, 2, 4],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 1]
]

for test_set in tests:
    result = remove_duplicates(test_set)
    assert result == [1, 3, 4], f"AssertionError: {! The result should be [1, 3, 4] not {test_set}"
```
The above Python script defines a function `remove_duplicates` that takes a list of integers as input and removes all duplicate elements from it. The tests section contains a list of test cases, each of which is passed through the function and the resulting output is compared with the expected output. The script also includes an series of assertions that check the correctness of the `remove_duplicates` function.