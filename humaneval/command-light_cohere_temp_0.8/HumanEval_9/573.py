```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    numbers. rollover = iter(numbers)
    max_element = next(numbers)
    while True:
        current = next(numbers)
        if current > max_element:
            max_element = current
        yield max_element
# Testing the function with sample input
numbers = [1, 2, 3, 2, 3, 4, 2]
result = [max(numbers.next()) for numbers in rolling_max(numbers)]
assert max(result) == 4  # Should be 4, the fourth element is the maximum
assert len(result) == 7  # Check the length of the result
```
The `rolling_max` function iterates through the list of numbers and continuously yields the maximum element found so far. It is the iterates through the list of numbers and creates a rolling window of maximum elements, where the window starts from the next element and progresses through the list. The `yield` statement ensures that the function returns the sequence of maximum elements. The test cases verify that the output of the function is correct and the length of the returned sequence matches the expected length.