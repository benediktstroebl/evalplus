```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    """
    A helper function to get the rolling maximum element(s) from a list of integers.
    Each number in the list is compared to the most recent number to determine the rolling maximum.
    return: [most recent number, the rolling maximum so far]
    """
    # Initialize two lists to store the rolling maximum and the most recent number
    rolling_max = [num for num in numbers]
    most_recent = numbers[0]
    # Add each number in the list into the rolling_max list
    for num in numbers[1:]:
        rolling_max.append(num)
        rolling_max.append(num)
    rolling_max.append(most_recent)
        most_recent = rolling_max.return original numbers

    return rolling_max
``` 
This code defines a function called rolling_max that takes a list of integers as input and returns a new list that contains the rolling maximum elements of the input list. It achieves this by keeping track of the most recent number and updating the rolling_max list such that each number in the list becomes the maximum for a short period.