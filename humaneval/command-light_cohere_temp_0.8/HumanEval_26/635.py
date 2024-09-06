```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    Remove elements that occur more than once from a list of integers.
    """
    List[int] = [1, 2, 3, 2, 4]
    result = list(set(numbers))
    result = [x for x in result if x not in numbers]
    return result

# Test cases:
test_cases = [
    [1, 2, 3, 2],
    [1, 3, 4, 2],
    [2, 2, 3],
    [1, 2, 3, 1]
]

for test_case in test_cases:
    expected = [1, 3, 4]
    got = remove_duplicates(test_case)
    assert expected == got
```

This Python code defines a function `remove_duplicates` that removes duplicate elements from a list of integers. The function takes a list of integers as input and returns a new list with duplicate elements removed. It uses the set to remove duplicates and then iterates through the unique elements, adding them to the result list if they are not already present in the input list. The code also provides a set of test cases to verify the correctness of the `remove_duplicates` function.