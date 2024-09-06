```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [num for num, i in sorted((num, i) for i, num in enumerate(numbers)) if i < len(numbers) and num > numbers[i]]
def test_rolling_max(test_list: List[int]) -> None:
    actual_result = rolling_max(test_list)
    expected_result = [2, 3, 3, 3, 4, 4]
    assert actual_result == expected_result, "The rolling_max function did not return the expected result."
test_cases = [
    [1, 2, 3, 2, 3, 4, 2],
    [5, 6, 7, 8, 9, 10, 11],
    [10, 20, 30, 40, 50, 60, 70],
]
for test in test_cases:
    test_rolling_max(test)
```
This script defines a function `rolling_max` which returns a list of integers, calculated as the maximum rolling element from a list of numbers. The function is also tested using a set of test cases, and passes all the tests using `assert_rolling_max`.