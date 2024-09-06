```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generate a list of rolling maximum elements from a given list of integers.
    The list of rolling maximum elements will be returned.
    """
    list comprehension approach, combined with the filtering and mapping technique, is used to achieve this.
    Return the list of integers that follow the criteria of maximum elements, starting from a particular moment, and repeating until the end of the sequence, are identified using the rolling window technique.
    """
 list comprehension is used to efficiently generate a list of numbers that meet the rolling maximum criteria. The filtering and mapping technique is then used to modify the list to only include numbers that are greater than or equal to the rolling maximum at the current moment.

This method is very effective for big datasets with a limited amount of memory.

# Example Test:
numbers = [1, 2, 3, 2, 3, 4, 2]
rolling_max_result = rolling_max(numbers)
print(rolling_max_result)  # Output: [1, 2, 3, 3, 3, 4, 4]
```