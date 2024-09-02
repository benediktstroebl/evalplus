from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    previous_maximum = None
    maximums = []

    for number in numbers:
        if previous_maximum is None:
            previous_maximum = number
            maximums.append(previous_maximum)
        else:
            if number >= previous_maximum:
                previous_maximum = number
            maximums.append(previous_maximum)

    
