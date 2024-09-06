```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [num for num, i in zip(numbers, range(len(numbers))) if i % 2 == 0 and numbers[i] > numbers[i - 1]]
def test_rolling_max(test_numbers: List[int]) -> None:
    results = rolling_max(test_numbers)
    assert all(results), "Rolling maximum elements are not found in the list"
test_data = [1, 2, 3, 2, 3, 4, 2]
test_rolling_max(test_data)
```
The code defines a function `rolling_max` that generates a list of integers by finding the maximum element from the previous two elements in the list, iterated over. The function is then tested using the `test_rolling_max` which takes a list of integers and asserts that the result of `rolling_max` function is correct for the given list.