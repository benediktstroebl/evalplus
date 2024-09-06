```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [x for x, n in zip(numbers, numbers) if n >= x or x == numbers[0]]
def test_rolling_max(test_numbers: List[int]) -> None:
    assert rolling_max(test_numbers) == [x for x, _ in test_numbers if x > 0], "Function doesn't return correct rolling max"
    return
test_rolling_max([1, 2, 3, 2, 3, 4, 2])
``` 
This Python code defines a function `rolling_max` that computes the rolling maximum element in a list of integers. The `rolling_max` function uses a generator expression to track the maximum elements, and it filters out any duplicates or numbers equal to the first element in the list. The `test_rolling_max` function serves to validate the correctness of the `rolling_max` function by providing a test case that involves a list of test numbers, and it checks if the function returns the correct results.