from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    # Initialize the empty list that will store the rolling maxima
    rolling_maxima = []
    # Initialize the current_maximum variable to the first element of the list
    current_maximum = numbers[0]
    # Initialize the current_index to 0
    current_index = 0
    # Loop over the list
    for index in range(1, len(numbers)):
        # Check if the current element is larger than the current maximum
        if numbers[index] > current_maximum:
            # If yes, update the current maximum
            current_maximum = numbers[index]
            # If yes, update the current index
            current_index = index
        # Add the current maximum to the rolling maxima list
        rolling_maxima.append(current_maximum)
    # Return the rolling maxima list
    return rolling_maxima

