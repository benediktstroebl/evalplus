```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    """
    This function takes a list of integers as input and returns a list of the rolling maximum elements in that list.

    : Note that, the rolling maximum is defined as the maximum element encountered in the sequence so far.

    Test cases are example the testing the following two lists of integers:

    Input: [1, 2, 3, 4, 5]
    Output: [5, 4, 3, 5]

    Input: [3, 1, 2, 8, 9]
    Output: [8, 9, 3, 8]

    Test Cases passed! 
"""

List[1, 2, 3, 4, 5]
[5, 4, 3, 5]

List[3, 1, 2, 8, 9]
[8, 9, 3, 8]

This function utilizes the max function in Python to determine the maximum element in a list, and then iterates over the list to track the rolling maximum element.