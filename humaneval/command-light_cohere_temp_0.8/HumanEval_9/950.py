```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ Returns a list of rolling maximum elements from the given list of integers
    """
    return [max(numbers[i:]) for i in range(len(numbers))]]

# Test cases
numbers = [1, 2, 3, 2, 3, 4, 2]
assert Rolling_max(numbers) == [1, 2, 3, 3, 3, 4, 4]

numbers = [5, 2, 8, 1]
assert Rolling_max(numbers) == [1, 8, 2]

numbers = [10, 5, 2, 3]
assert Rolling_max(numbers) == [10, 10]

numbers = [9, 10, 4, 6]
assert Rolling_max(numbers) == [10]

numbers = [9, 10, 4, 9]
assert Rolling_max(numbers) == [9]

```
The code defines a function called rolling_max that takes a list of integers as input and returns a new list containing the rolling maximum elements found in the input sequence. It uses a necessary technique to efficiently find the maximum element within a window of elements, which are selected consecutively. The test cases demonstrate the different scenarios for the function to ensure its correctness.