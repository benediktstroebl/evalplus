```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    numbers.remove_duplies(numbers)
    return [x for x in sorted(numbers) if x != numbers[-1]] + [numbers[-1]]
def test_rolling_max(test_numbers: List[int]) -> None:
    actual_rolling_max = rolling_max(test_numbers)
    expected_rolling_max = [x for x in reversed(test_numbers) if x != test_numbers[-1]] + [test_numbers[-1]]
    assert actual_rolling_max == expected_rolling_max, "Actual and expected rolling_max lists do not match."
```
This code defines a function `rolling_max` that calculates the rolling maximum elements of a list of integers. It uses the same list comprehension and a generator expression to iterate through the sorted list of numbers, excluding the last element (the one just removed). The function also removes duplicate numbers from the input list. 

The `test_rolling_max` function is a test case for the `rolling_max` function. It takes two list of integers, creates the `rolling_max` function, and then compares the result with the expected rolling maximum elements. 

The test case succeeds if the actual and expected rolling maximum lists match.