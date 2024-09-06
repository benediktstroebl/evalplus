```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [x for x, n in zip(numbers, numbers) if n >= x or n == numbers[0]]
def test_rolling_max(test_numbers: List[int]) -> None:
    actual_result = rolling_max(test_numbers)
    expected_result = [n for n in test_numbers if n == max(test_numbers) or n >= max(test_numbers)]
    assert actual_result == expected_result, " Rolling maximum function failed test"

# Test the function
test_numbers = [1, 2, 3, 2, 3, 4, 4]
test_rolling_max(test_numbers)
```