```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generate a list of rolling max elements found until a given moment in the sequence.
    :param numbers: list of integers
    :return: list of rolling max elements
    """
    # initialize the rolling window maximum list and index
    rolling_max_lst = [num for num in numbers]
    rolling_max_index = 0

    # loop until the end of the numbers list is reached
    while rolling_max_index < len(numbers) - 1:
        # get the current maximum element
        current_max = rolling_max_lst[rolling_max_index]

        # check if the current element is greater than the rolling_max
        if numbers[rolling_max_index + 1] > current_max:
            current_max = numbers[rolling_max_index + 1]

        # add the current maximum element to the rolling_max list
        rolling_max_lst.append(current_max)

        # increment the rolling_max index
        rolling_max_index += 1

    return rolling_max_lst
```
The code defines a function called `rolling_max` that takes a list of integers as input and returns a new list of integers, which represents the rolling maximum elements found in the input list up to the given moment.