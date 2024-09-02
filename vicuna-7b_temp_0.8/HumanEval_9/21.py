from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    # Initialize empty list for the rolling maximum
    rolling_max_list = []
    # Iterate through the list of numbers
    for i in range(1, len(numbers)):
        # Get the maximum element from the rolling window of size i
        rolling_max_list.append(max(numbers[i:i+i+1]))
    return rolling_max_list