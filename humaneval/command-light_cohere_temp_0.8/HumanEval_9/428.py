```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum elements found until the given moment in the sequence.
    : Return the maximum rolling element over a given sequence until the current index reaches the end.
    """

    list of rolling maximum elements is returned.

Example:
numbers = [1, 2, 3, 2, 3, 4, 2]
rolling_max_elements = rolling_max(numbers)
print(rolling_max_elements)  # Output: [1, 2, 3, 3, 3, 4, 4]

test_passes = [
    [1, 3, 4, 5, 6],  # [5, 6] is the maximum in this sublist, but it's not the last element.
    [1, 2, 3, 4, 5, 6],  # [2, 3, 4, 5] is the correct answer.
    [1, 2, 3, 3, 4, 5],  # Incorrect, [5] is the last element, not the maximum.
    [1, 2, 3, 3, 4, 5, 6, 7]  # Another test case

def test(numbers: List[int]) -> bool:
    return rolling_max(numbers) == numbers

```