```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    A list of integers is given, along with a start moment.
    """
    rolling_max(numbers) generates a list of rolling maximum elements from the start moment until the end of the sequence is reached.
    """The rolling_max function takes a list of integers and uses the list's `append` method to generate a new list. This new list contains theze rolling maximum elements from the start moment until the end of the sequence is reached.
    return:
    A list of integers.

Test Cases:
>>> numbers = [1, 2, 3, 2, 3, 4, 2]
>>> rolling_max(numbers)
[1, 2, 3, 3, 3, 4, 4]

>>> numbers = [5, 6, 4, 7, 8]
>>> rolling_max(numbers)
[8, 7, 6, 5]
```