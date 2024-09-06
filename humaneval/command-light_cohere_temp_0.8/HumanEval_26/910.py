```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    return [n for n in numbers if n < numbers.count(n)]


# Sample test cases
test_cases = [
    [1, 2, 3, 2, 4],
    [1, 2, 3, 4, 5, 2],
    [5, 6, 5, 7],
    [1, 2, 3, 1]
]

for test_case in test_cases:
    actual = remove_duplicates(test_case)
    expected = [1, 3, 4]
    assert actual == expected, f"AssertionError: {actual} != {expected}"
```
This Python code defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with elements that appear at most once removed. 

It utilizes the `count()` method to find duplicates and then filters the input list accordingly.  The function is tested using sample test cases, passing each test case into the `remove_duplicates` function and comparing the returned list with the expected list.